import re
from utils import html2text, simple_get, log_actions

"""
Find all the books url in the txt
starts with "https://nashremahi.com/book/ and ends with /"
"""

def get_book_urls_mahi(txt):
    book_urls = re.findall(r'https://nashremahi.com/book/[^/]+/', txt)
    return book_urls

def get_book_urls_30book(txt):
    # If starts with /book/ and ends with "> after find remvoe ">
    book_urls = re.findall(r'/book/[^>]+>', txt)
    book_urls = ["https://30book.com"+url.replace('">', '') for url in book_urls]
    return book_urls

def prosessPage_30book(url):
    resp = simple_get(url)
    if resp is not None:
        text = html2text(resp)
    else:
        log_actions(
            "No response for url: {}".format(url)
        )
        return None
    # Remove all 2 or more new lines
    text = re.sub(r'\n{2,}', '\n', text)
    # Remove all spaaces more than one
    text = re.sub(r'\s{2,}', '\n', text)

    # author: If starts with نویسنده:
    # There is only one author
    if "نویسنده:" in text:
        author = re.findall(r'نویسنده:[^\n]+', text)
        if len(author) == 0:
            author = "Unknown"
        else:
            author = author[0].replace("نویسنده:", "").strip()
    elif "نویسندگان:" in text:
        author = re.findall(r'نویسندگان:[^\n]+', text)
        if len(author) == 0:
            author = "Unknown"
        else:
            author = author[0].replace("نویسندگان:", "").strip()
        temps = re.findall(r'{0}[^\n]+'.format(author.split()[0]), text)
        # if any contains ، select and split it
        if len(author) == 0:
            author = "Unknown"
        else:
            for i in temps:
                if "،" in i:
                    author = i.split("،")
                    break
    else:
        author = "Unknown"


    # title: It starts with خرید کتاب and ends with اثر
    title = re.findall(r'خرید کتاب[^\n]+اثر', text)
    if len(title) == 0:
        title = "Unknown"
    else:
        title = title[0].replace("خرید کتاب", "").replace("اثر", "")
    # Translator: If starts with مترجم:
    translator = re.findall(r'مترجم:[^\n]+', text)
    if "مترجم:" not in text:
        translator = None
    elif len(translator) == 0:
        translator = "Unknown"
    else:
        translator = translator[0].replace("مترجم:", "").strip()
    # ISBN: find number between 10 and 13 digits
    isbn = re.findall(r'\d{10,13}', text)
    if len(isbn) == 0:
        isbn = "Unknown"
    else:
        isbn = isbn[0]
    # Publisher: Is starts with نشر: and new line after it
    publisher = re.findall(r'نشر:\n[^\n]+', text)
    if len(publisher) == 0:
        publisher = "Unknown"
    else:
        publisher = publisher[0].replace("نشر:", "").replace("\n", "")
    
    coverTypes = [
        "رحلی بزرگ", "رحلی کوچک", "خشتی", 
        "۲۴×۱۶/۸", "رقعی", "جیبی", "پالتویی",
    ]
    # If any of the coverTypes in the text assign it to coverType
    coverType = "Unknown"
    if "جلد کتاب" in text:
        for coverType in coverTypes:
            if coverType in text:
                coverType = coverType
                break
    # If coverType is not assigned assign it to Unknown
    if coverType is None:
        coverType = "Unknown"

    sizeTypes = [
        "قطع", "وزیری", "وزیری جدید", "پالتویی", "رحلی", "خشتی", "جیبی"
    ]
    # If any of the sizeTypes in the text assign it to sizeType
    sizeType = "Unknown"
    if "قطع کتاب" in text:
        for sizeType in sizeTypes:
            if sizeType in text:
                sizeType = sizeType
                break
    # If sizeType is not assigned assign it to Unknown
    if sizeType is None:
        sizeType = "Unknown"

    # Pages Count: is numbers before صفحه
    pagesCount = re.findall(r'\d+ صفحه', text)
    pagesCount = "Unknown"
    if len(pagesCount) == 0:
        pagesCount = "Unknown"
    else:
        pagesCount = pagesCount[0].replace("صفحه", "")
    # Code after book/ in url
    code = re.findall(r'book/[^/]+/', url)
    code = code[0].replace("book/", "").replace("/", "")
    coverUrl = f"https://www.30book.com/Media/Book/{code}.jpg"
    info = {
        "title": title.strip(),
        "author": author,
        "translator": translator,
        "isbn": isbn.strip(),
        "publisher": publisher.strip(),
        "coverType": coverType,
        "sizeType": sizeType,
        "pagesCount": pagesCount.strip(),
        "url": url,
        "coverUrl": coverUrl,
    }
    file_test = open("temp/test.txt", "w")
    file_test.write(text)
    return info