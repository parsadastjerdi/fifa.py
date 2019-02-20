from datetime import datetime, timedelta
from requests import get
from requests.exceptions import RequestException
import os, sys

# see if beautifulsoup is a better option than just regular requests
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
    'origin': ('https://fbref.com')
}


def get_json(endpoint, params, referer='scores'):
    '''
    Gets the json object 
    Input:
        endpoint:
        params:
        referer:
    Output:
        json (json): json object for the selected api call
    '''

    headers = dict(HEADERS)
    headers['referer'] = 'https://fbref.com/{ref}/'.format(ref=referer)
    html = get(BASE_URL.format(endpoint=endpoint, params=params))
    html.raise_for_status() # check to see if the html request was successful

    return html.json()


def api_scrape(json, index):
    '''
    Check this method to show that it actually works
    Input:

    Output:

    '''
    
    try:
        headers = json['results'][index]['headers']
        values = json['results'][index]['rowSet'] 
    except KeyError:
        # add for results that only include one set
        headers = json['results']['headers'] 
        values = json['results']['rowSet']  
    
    # return a pandas dataframe 
    if HAS_PANDAS:
        return DataFrame(values, columns=headers)
    else:
        # Taken from www.github.com/bradleyfay/py-goldsberry
        return [dict(zip(headers, value)) for value in values]        



if __name__ == '__main__':
    endpoint = 'players/d70ce98e/Lionel-Messi'
    league_id = 'squads/'
    seasons = 'comp/'
    params = {'LeagueID': league_id, 'Season': seasons}
    json = get_json(endpoint, params)

    