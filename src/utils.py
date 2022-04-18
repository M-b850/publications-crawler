import time, sys

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def html2text(html):
    """
    Convert HTML to text
    """
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    print(e)

def log_actions(action):
    print(action)
    log = open("temp/requests.log", "a")
    log.write(
        "{}: - {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), action)
        )
    log.close()

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
