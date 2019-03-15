from datetime import datetime

from requests import get, head
from requests.exceptions import RequestException

HAS_PANDAS = True
try:
    from pandas import DataFrame
except ImportError:
    HAS_PANDAS = False


TODAY = datetime.today()
BASE_URL = 'https://foxsports.com/soccer/{endpoint}'

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('https://foxsports.com/soccer/')
}


# need to find the correct referer
def _get_json(endpoint, params, referer='stats', **kwargs):
    '''
    Gets the json object 
    Input:
        endpoint:
        params:
        referer:
    Output:
        json (json): json object for the selected api call
    '''

    h = dict(HEADERS)
    h['referer'] = 'https://foxsports.com/{ref}/'.format(ref=referer)
    url = BASE_URL.format(endpoint=endpoint)
    print(url)

    response = get(url, params=params, headers=h)
    response.raise_for_status() 
    print(response.url)

    return response.json()

if __name__ == '__main__':
    endpoint = 'stats'
    params = {'competition': '1','season': '2018', 'category': 'STANDARD'}

    json = _get_json(endpoint=endpoint, params=params)
    print(json)

  