import re


"""
Find all the books url in the txt
starts with "https://nashremahi.com/book/ and ends with /"
"""
def get_book_urls(txt):
    book_urls = re.findall(r'https://nashremahi.com/book/[^/]+/', txt)
    return book_urls

