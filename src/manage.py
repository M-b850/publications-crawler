# Path: src/main.py
import time, sys
from handler import *
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


class Crawl:

    def get_next_page_url(self, page_number):
        base_url = 'https://nashremahi.com/shop/page/{}/'.format(page_number)
        return base_url

    def log_error(self, e):
        print(e)

    def log_actions(self, action):
        print(action)
        log = open("temp/requests.log", "a")
        log.write(
            "{}: - {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), action)
            )
        log.close()

    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def simple_get(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def get_page_string_data(self, url):
        """
        Get the data of the page
        """
        content = self.simple_get(url)
        # Convert the bytes response to a string
        content = content.decode('utf-8')
        return content

    def extract_book_urls(self, url, function_name):
        """
        Extract the book urls from the page
        """
        content = self.get_page_string_data(url)
        book_urls = function_name(content)
        return book_urls


def main():
    """
    Main function
    """
    while True:
        crawl = Crawl()
        current_page_number = 1
        page = crawl.get_next_page_url(current_page_number)
        book_urls = crawl.extract_book_urls(page, get_book_urls_mahi)
        if len(book_urls) == 0:
            crawl.log_actions('No more book urls')
            break
        for book_url in book_urls:
            print(book_url)


if __name__ == '__main__':
    main()
