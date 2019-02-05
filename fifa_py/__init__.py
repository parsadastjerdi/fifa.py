# Script is forked from 
from datetime import datetime, timedelta
import os

from requests import get
from nba_py.constants import League

HAS_PANDAS = True
try:
    from pandas import DataFrame
except ImportError:
    HAS_PANDAS = False

HAS_REQUESTS_CACHE = True
CACHE_EXPIRE_MINUTES = int(os.getenv('FIFA_PY_CACHE_EXPIRE_MINUTES', 10))
try:
    from requests_cache import install_cache
    install_cache(cache_name='fifa_cache',
                  expire_after=timedelta(minutes=CACHE_EXPIRE_MINUTES))
except ImportError:
    HAS_REQUESTS_CACHE = False

# Constants
TODAY = datetime.today()
BASE_URL = 'https://stats.fbref.com/{endpoint}'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('https://fbref.com')
    }


def _api_scrape(json_inp, ndx):
    '''
    Internal method to streamline the getting of data from the json
    Args:
        json_inp (json): json input from our caller
        ndx (int): index where the data is located in the api
    Returns:
        If pandas is present:
            DataFrame (pandas.DataFrame): data set from ndx within the
            API's json
        else:
            A dictionary of both headers and values from the page
    '''
    pass



def _get_json(endpoint, params, referer='scores'):
    '''
    Internal method to streamline our requests / json getting
    Args:
        endpoint (str): endpoint to be called from the API
        params (dict): parameters to be passed to the API
    Raises:
        HTTPError: if requests hits a status code != 200
    Returns:
        json (json): json object for selected API call
    '''
    h = dict(HEADERS)
    h['referer'] = 'http://fbref.com/{ref}/'.format(ref=referer)
    _get = get(BASE_URL.format(endpoint=endpoint), params=params,
               headers=h)
    # print _get.url
    _get.raise_for_status()
    return _get.json()


# Adjust this for multiple leagues and multiple teams within leagues
class Scoreboard:
    '''
    A scoreboard for all games for a given day
    Displays current games plus info for a given day
    Args:
        :month: Specified month (1-12)
        :day: Specified day (1-31)
        :year: Specified year (YYYY)
        :league_id: ID for the league to look in (Default is 00)
        :offset: Day offset from which to operate
    Attributes:
        :json: Contains the full json dump to play around with
    '''
    _endpoint = 'scoreboard'

    def __init__(self,
                 month=TODAY.month,
                 day=TODAY.day,
                 year=TODAY.year,
                 league_id=League.DEFAULT,
                 offset=0):
        self._game_date = '{month:02d}/{day:02d}/{year}'.format(month=month,
                                                                day=day,
                                                                year=year)
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'GameDate': self._game_date,
                                      'DayOffset': offset})

    def game_header(self):
        return _api_scrape(self.json, 0)

    def line_score(self):
        return _api_scrape(self.json, 1)

    def series_standings(self):
        return _api_scrape(self.json, 2)

    def last_meeting(self):
        return _api_scrape(self.json, 3)

    def available(self):
        return _api_scrape(self.json, 4)