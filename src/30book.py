'''
Links that contains books:
    [X] 1. https://www.30book.com/category/BTA-1-3/%D8%A7%D8%AF%D8%A8%DB%8C%D8%A7%D8%AA/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    [X] 2. https://www.30book.com/category/BTA-1-16/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    [X] 3. https://www.30book.com/category/BTA-1-24/%D9%BE%D8%B2%D8%B4%DA%A9%DB%8C-%D9%88-%D8%B1%D9%88%D8%A7%D9%86-%D8%AF%D8%B1%D9%85%D8%A7%D9%86%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    [X] 4. https://www.30book.com/category/BTA-1-1/%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    5. https://www.30book.com/category/BTA-1-10/%D8%AD%D9%82%D9%88%D9%82%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    6. https://www.30book.com/category/BTA-1-7/%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    7. https://www.30book.com/category/BTA-1-11/%D8%B2%D9%86%D8%AF%DA%AF%DB%8C-%D9%86%D8%A7%D9%85%D9%87-%D9%88-%D8%AE%D8%A7%D8%B7%D8%B1%D9%87/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    8. https://www.30book.com/category/BTA-1-18/%D8%B3%D8%A8%DA%A9-%D8%B2%D9%86%D8%AF%DA%AF%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    9. https://www.30book.com/category/BTA-1-5/%D8%B3%DB%8C%D8%A7%D8%B3%D8%AA/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    10. https://www.30book.com/category/BTA-1-17/%D8%B3%DB%8C%D9%86%D9%85%D8%A7-%D9%88-%D8%AA%D8%A6%D8%A7%D8%AA%D8%B1/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    11. https://www.30book.com/category/BTA-1-21/%D8%B7%D9%86%D8%B2/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    12. https://www.30book.com/category/BTA-1-25/%D8%B9%D9%84%D9%85%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    13. https://www.30book.com/category/BTA-1-8/%D8%B9%D9%84%D9%88%D9%85-%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    14. https://www.30book.com/category/BTA-1-13/%D9%81%D8%B1%D9%87%D9%86%DA%AF%D8%8C-%D9%85%D8%B1%D8%AC%D8%B9-%D9%88-%D8%AF%D8%A7%DB%8C%D8%B1%D8%AA-%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D8%B1%D9%81/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    15. https://www.30book.com/category/BTA-1-6/%D9%81%D9%84%D8%B3%D9%81%D9%87/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
    16. https://www.30book.com/category/BTA-1-27/%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1-%D9%88-%D8%AA%DA%A9%D9%86%D9%88%D9%84%D9%88%DA%98%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C
'''
import os
import json

from manage import Crawl
from handler import get_book_urls_30book, prosessPage_30book


urls = [
    
    'https://www.30book.com/category/BTA-1-13/%D9%81%D8%B1%D9%87%D9%86%DA%AF%D8%8C-%D9%85%D8%B1%D8%AC%D8%B9-%D9%88-%D8%AF%D8%A7%DB%8C%D8%B1%D8%AA-%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D8%B1%D9%81/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C',
    'https://www.30book.com/category/BTA-1-6/%D9%81%D9%84%D8%B3%D9%81%D9%87/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C',
    'https://www.30book.com/category/BTA-1-27/%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1-%D9%88-%D8%AA%DA%A9%D9%86%D9%88%D9%84%D9%88%DA%98%DB%8C/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C',
]

# Override get_next_page_url function
def get_next_page_url(url, page_number):
    items = url + "?cQ=False&cD=False&cS=False&st=7&stO=True&pg=&ps=60000&qWriter=0&qInter=0&qPub=0&qTs=0&qTa=0&qTf=0"
    return items

crawl = Crawl()
crawl.get_next_page_url = get_next_page_url
crawl.get_book_info = None

def main():
    DIR = os.path.dirname(os.path.abspath(__file__))
    print(DIR)
    file = open("temp/book-urls.txt", "a")

    print("Start crawling...")
    for url in urls:
        current_page_number = 1
        page = crawl.get_next_page_url(url, current_page_number)
        book_urls = crawl.extract_book_urls(page, get_book_urls_30book)
        log_text = """
                url: {}
                page: {}
                count: {}
                """.format(url, current_page_number, len(book_urls))
        crawl.log_actions(log_text)

        if len(book_urls) == 0:
            crawl.log_actions('No more book urls')
            # break
        else:
            for book_url in book_urls:
                if book_url not in open("temp/book-urls.txt").read():
                    file.write(book_url + "\n")
                    file.flush()


def collect(url):
    if url != "":
        info = prosessPage_30book(url)
        if info != None:
            return info
        else:
            crawl.log_actions("No info for url: {}".format(url))

if __name__ == '__main__':
    line_number = 0

    # main()
    urls = open("temp/book-urls.txt").read().split("\n")
    # book-urls
    for url in urls:
        r = collect(url)
        # Chck if the book is already in the database
        
        # add dict to book-info.json
        with open("temp/book-info.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "," + "\n")
            line_number += 1
            f.flush()
            file = open("temp/line_numer.txt", "w+", encoding="utf-8")
            file.write(str(line_number))
