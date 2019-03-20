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
    Parses the JSON retrieved from the API into a more usable format
    
    Args:
        json: json object 
        key: specific key to index from the json object
        exclude: list of keys to exclude from the json object
    Returns:
        pandas dataframe 
    Raises:
    Notes:
        - Try catch is due to having some dataframes with only one index (need to hardcode that index==0)
        - for loop is used for key so that multiple layered json objects can be indexed
    '''
    if key is not None:
        for k in key:
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
    Streamlines getting JSON from API. This only includes free tier leagues for now, since
    I don't have access to any of the paid tier resources.

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
    '''
    include['api_token'] = api_key
    r = get(BASE_URL.format(endpoint=endpoint), params=include)
    r.raise_for_status()
    print(r.url)
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


def info(response):
    '''
    Prints response header information

    Args:
        response: HTTP response
    Returns:
        None
    Raises:
        None
    '''
    print('Response Headers:')
    # print('API Version:', response.headers['X-API-Version'])
    # print('Client:', response.headers['X-Authenticated-Client'])
    # print('Seconds to reset counter:', response.headers['X-RequestCounter-Reset'])
    # print('Requests Available:', response.headers['X-Requests-Available-Minute'])


def get_key(self):
