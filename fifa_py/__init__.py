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


# TODO: import requests cache at later point

TODAY = datetime.today()
BASE_URL = 'https://stats.fbref.com/{endpoint}'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('https://fbref.com/en/')
    }


def _get_json(endpoint, params, referer='scores'):
    headers = dict(HEADERS)
    headers['referer'] = 'https://fbref.com/{ref}/'.format(ref=referer)
    html = get(BASE_URL.format(endpoint=endpoint, params=params))
    html.raise_for_status()
    return html.json()


def get_json(endpoint, params, referer='scores'):
    url = BASE_URL + endpoint

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

    return 'None'   


if __name__ == '__main__':
    endpoint = 'players/d70ce98e/Lionel-Messi'
    league_id = 'squads/'
    seasons = 'comp/'
    params = {'LeagueID': league_id, 'Season': season}
    json = get_json(endpoint, params)

    