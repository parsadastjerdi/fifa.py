from requests import get
from requests.exceptions import RequestException

from pandas import DataFrame

BASE_URL = 'https://api.football-data.org/v2/{endpoint}'

key = open('../.api-key').read().strip()
HEADERS = {
    'X-Auth-Token': key
}


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
        Separate val
    '''
    if key is not None:
        json = json[key]

    if exclude is None:
        return DataFrame(json, index=[0])

    for key in exclude:
        json.pop(key)

    return DataFrame(json, index=[0])


def _get_json(endpoint, filters=dict(), **kwargs):
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

    filters['plan'] = 'TIER_ONE'
    h = dict(HEADERS)
    r = get(BASE_URL.format(endpoint=endpoint), params=filters, headers=h)
    r.raise_for_status()
    return r.json()



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
    print('API Version:', response.headers['X-API-Version'])
    print('Client:', response.headers['X-Authenticated-Client'])
    print('Seconds to reset counter:', response.headers['X-RequestCounter-Reset'])
    print('Requests Available:', response.headers['X-Requests-Available-Minute'])


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
        endpoint += '/' + str(h)
    return endpoint


if __name__ == '__main__':
    try:
        json = _get_json(endpoint='match')
        print(json.keys())

        """
        for comp in json['competitions']:
            print(comp['area']['name'], comp['name'] + ':', comp['id'])
        """

    except Exception as e:
        print(e)