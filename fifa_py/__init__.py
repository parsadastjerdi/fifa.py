'''
Script is based on __init__.py from nba_py. Project structure is based on the structure of nba_py as well.
'''

from datetime import datetime, timedelta
from requests import get
from requests.exceptions import RequestException
import os, sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('BeautifulSoup not found.')
    sys.exit(1)


try:
    from pandas import DataFrame
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

HAS_REQUESTS_CACHE = True
CACHE_EXPIRE_MINUTES = int(os.getenv('FIFA_PY_CACHE_EXPIRE_MINUTES', 10))
try:
    from requests_cache import install_cache
    install_cache(cache_name='fifa_cache', expire_after = timedelta(minutes=CACHE_EXPIRE_MINUTES))
except ImportError:
    HAS_REQUESTS_CACHE = False


TODAY = datetime.today()
BASE_URL = 'https://stats.fbref.com/{endpoint}'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('https://fbref.com')
    }


def api_scrape(json_input):
    endpoint = 'd70ce98e/Lionel-Messi'
    url = 'https://fbref.com/en/players/{endpoint}'.format(endpoint=endpoint)

    try:
        with get(url) as html:
            soup = BeautifulSoup(html.content, 'html.parser')
            for p in soup.find_all('div', attrs={'class':'p1'}):
                print(p.text)
            
            listhead = soup.find_all('ul', attrs={'class': 'grouplist'})
            print(listhead)

            # words = listhead.split('<li>')
            # try: 
                # temp = BeautifulSoup(words, 'html.parser')
            # except Exception as e: 
                # print('**ERROR**')
                # print(e)
            # print(len(temp))
            # for name in listhead.find('li'):
                # print(name.text)           
    except RequestException as e:
        print(e)


def get_json(endpoint, params, referer='scores'):
    headers = dict(HEADERS)
    headers['referer'] = 'https://fbref.com/{ref}/'.format(ref=referer)
    html = get(BASE_URL.format(endpoint=endpoint, params=params))
    html.raise_for_status()
    return html.json()


if __name__ == '__main__':
    api_scrape(0)
    