from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
    

if __name__ == '__main__':
    endpoint = 'd70ce98e/Lionel-Messi'
    url = 'https://fbref.com/en/players/{0}'.format(endpoint)

    try:
        html = get(url)
        print(type(html))
    except:
        print('html == None')
    
    soup = BeautifulSoup(html.content, 'html.parser')
    for p in soup.select('p'):
        print(p.text)



class Player:
    '''
    Returns player data and other stuff
    '''
    pass