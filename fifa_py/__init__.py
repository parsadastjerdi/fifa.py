from requests import get
from requests.exceptions import RequestException

HAS_PANDAS = True
try:
    from pandas import DataFrame
except:
    HAS_PANDAS = False

BASE_URL = 'https://soccer.sportmonks.com/api/v2.0/{endpoint}'

def _api_scrape(json, key, exclude, **kwargs):
    '''
    Parses the JSON retrieved from the API into a pandas DataFrame
    
    Args:
        json: json object 
        key: specific key to index from the json object
        exclude: list of keys to exclude from the json object
    Returns:
        pandas dataframe 
    Raises:

    Notes:
        - Try catch is due to having some dataframes with only one index (need to hardcode that index==[0])
        - for loop is used for key so that multiple layered json objects can be indexed
    '''
    if key is not None:
        for k in key:
            print(k)
            json = json[k]
    
    if exclude is not None:
        for k in exclude:
            json.pop(k)
    
    try:
        return DataFrame(json)
    except Exception:
        return DataFrame(json, index=[0])


def _get_json(endpoint, api_key, include=dict(), **kwargs):
    '''
    Streamlines getting JSON from API.

    Args:
        endpoint (str): endpoint to be called from the api
        filters (dict): parameters to be passed to the api

    Returns:
        json (json): json object for the selected api call

    Raises:
        HTTPError: if request status code != 200
        Exception: if the request code is malformed or bad

    Notes:
        Is h['referer'] necessary and should the old header be included as well?
        # need to take into account rate limiter when getting json, then call get again
        if r.status_code == 429:
            print('Rate limiting in effect. Waiting 1 minute until limiter resets.')
            sleep(60)
            r = get(BASE_URL.format(endpoint=endpoint), params=include)
    '''
    include['api_token'] = api_key
    r = get(BASE_URL.format(endpoint=endpoint), params=include)
    try:
        r.raise_for_status()
    except Exception as e:
        print(e)
        return None
    return r.json()


def _form_endpoint(hlist):
    '''
    Simple method to create endpoints from a list of headers

    Args:
        :hlist (list): list of headers to be concatendated
    Returns:
    Raises:
    '''

    endpoint = ''
    for h in hlist:
        endpoint += str(h) + '/'
    return endpoint


def _get_key():
    '''
    Testing method in order to not push api key to repo
    '''
    with open('../.api-key', 'r') as key:
        return key.read().strip()