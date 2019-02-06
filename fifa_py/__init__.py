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
    pass


def get_json(endpoint, params, referer='scores'):
    headers = dict(HEADERS)


