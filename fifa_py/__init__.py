from datetime import datetime

from requests import get, codes
from requests.exceptions import RequestException


HAS_PANDAS = True
try:
    from pandas import DataFrame
except ImportError:
    HAS_PANDAS = False


TODAY = datetime.today()
BASE_URL = 'https://api.football-data.org/v2/{endpoint}'

key = open('../.api-key').read().strip()
HEADERS = {
    'X-Auth-Token': key
}


class APIErrorException(Exception):
    pass


def _api_scrape(json, index):
    '''
    Parses the json retrieved from 
    
    Args:
    Returns:
    Raises:
    '''
    pass


def _get_json(endpoint, params, **kwargs):
    '''
    Streamlines getting json

    Args:
        endpoint (str): endpoint to be called from the api
        params (dict): parameters to be passed to the api

    Returns:
        json (json): json object for the selected api call

    Raises:
        HTTPError: if request status code != 200
        Exception: if the request code is malformed or bad

    Notes:
        Is h['referer'] necessary and should the old header be included as well?
    '''
    h = dict(HEADERS)
    r = get(BASE_URL.format(endpoint=endpoint), params=params, headers=h)
    r.raise_for_status()
    
    # exception handling: https://github.com/architv/soccer-cli/blob/master/soccer/request_handler.py
    if r.status_code == codes.ok:
        return r.json()

    elif r.status_code == codes.bad:
        raise APIErrorException('Invalid request. Check parameters.')

    elif r.status_code == codes.forbidden:
        raise APIErrorException('This resource is restricted')

    elif r.status_code == codes.not_found:
        raise APIErrorException('This resource does not exist. Check parameters')

    elif r.status_code == codes.too_many_requests:
        raise APIErrorException('You have exceeded your allowed requests per minute/day')



def debug(response):
    '''
    Prints response header information

    Args:

    Returns:
        None
    Raises:
        None
    '''
    print('Response Headers:')
    print('API Version:', response.headers['X-API-Version'])
    print('Client:', response.headers['X-Authenticated-Client'])
    print('Seconds to reset counter:', response.headers['X-RequestCounter-Reset'])
    print('Requests Available:', response.headers['X-Requests-Available-Minute'])


if __name__ == '__main__':
    try:
        json = _get_json(endpoint='competitions/PL/matches', params={'matchday':10})
        print(json)
    except Exception as e:
        print(e)
