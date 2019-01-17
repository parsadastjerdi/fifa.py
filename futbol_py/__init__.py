# Script is based off of https://github.com/sports-analytics/nba_py/blob/master/nba_py/__init__.py

from datetime import datetime, timedelta
import os

from requests import get
# from futbol_py.constants import League

HAS_PANDAS = True
try:
    from pandas import DataFrame
except ImportError:
    HAS_PANDAS = False

HAS_REQUESTS_CACHE = True
CACHE_EXPIRE_MINUTES = int(os.getenv('SOCCER_PY_CACHE_EXPIRE_MINUTES', 10))

try:
    from requests_cache import install_cache
    install_cache(cache_name='soccer_cache',
                  expire_after = timedelta(minutes = CACHE_EXPIRE_MINUTES))
except ImportError:
    HAS_REQUESTS_CACHE = False

# Constants
# TODAY = datetime.today()
BASE_URL = 'https://fbref.com/{endpoint}'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('https://fbref.com')
}


def api_scrape(json_input, index):

    """
        Internal method to get data from json

        Args: 
            json_input (json): json input from the caller
            index (int): index where the data is located in the api

        Returns:
            if pandas is present:
                Dataframe (panda.DataFrame): data set from index within the API's json
            else:
                A dict of both headers and values from the page
    """

    try:
        headers = json_input['resultSets'][index]['headers']
        values = json_input['resultSets'][index]['rowSet']

    except KeyError:
        # This is so ugly but this is what you get when your data comes out
        # in not a standard format
        try:
            headers = json_input['resultSet'][index]['headers']
            values = json_input['resultSet'][index]['rowSet']
        except KeyError:
            # Added for results that only include one set (ex. LeagueLeaders)
            headers = json_input['resultSet']['headers']
            values = json_input['resultSet']['rowSet']
    if HAS_PANDAS:
        return DataFrame(values, columns=headers)
    else:
        # Taken from www.github.com/bradleyfay/py-goldsberry
        return [dict(zip(headers, value)) for value in values]


def get_json():
    pass
