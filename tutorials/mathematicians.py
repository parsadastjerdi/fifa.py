from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    '''
    Attempts to get the url by making an HTTP get request
    '''
    try:
        # closing function ensures that any network resources are freed
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))

def is_good_response(resp):
    '''
    returns true if the response is HTML, else false
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
    
def log_error(e):
    print(e)

def get_names():
    url = ''
    html = simple_get(url)
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        names = set()
        for li in soup.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

def get_hits_on(name):
    

if __name__ == '__main__':
    html = my_get('https://realpython.com/blog/')
    soup = BeautifulSoup(html, 'html.parser')
    for p in soup.select('p'):
        print(p.text)
