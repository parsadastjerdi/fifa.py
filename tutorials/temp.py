from datetime import datetime, timedelta
from requests import get
from requests.exceptions import RequestException
import os, sys

from bs4 import BeautifulSoup

def test(endpoint, params, referer='scores'):
    '''
        get json object 
    url = BASE_URL.format(endpoint=endpoint)

    try:
        with get(url) as html:
            soup = BeautifulSoup(html.content, 'html.parser')

            for p in soup.find_all('div', attrs={'class':'p1'}):
                print(p.text)
            
            listhead = soup.find_all('ul', attrs={'class': 'grouplist'})
            print(listhead)

            # words = listhead.split('<li>')
            # try: 
                # temp = BeautifulSoup(words, 'html.parser')
            # except Exception as e: 
                # print('**ERROR**')
                # print(e)
            # print(len(temp))
            # for name in listhead.find('li'):
                # print(name.text)           
    except RequestException as e:
        print(e)
    '''
    return 'None' 

url = 'https://fbref.com/en/squads/'
html = get(url)
soup = BeautifulSoup(html.content, 'html.parser')
leagues = soup.find_all('td', attrs={'class': 'left', 'data-stat': 'competitions'}) # check this split
links = leagues.find('a')
print(len(leagues))
for league in leagues:
    print(league)
    print()


'''
<tr>
    <th scope="row" class="left " data-stat="country" >
        <a href="/en/squads/country/ENG/England-Football-Clubs">England Football Clubs</a>
    </th>

    <td class="right iz" data-stat="flag" >
        <span class="f-i f-gb-eng">eng</span> 
    </td>

    <td class="right " data-stat="num_clubs" > 154 </td>

    <td class="left " data-stat="competitions" >
        <a href="/en/comps/9/Premier-League-Seasons">Premier League</a>, 
        <a href="/en/comps/10/EFL-Championship-Seasons">EFL Championship</a>, 
        <a href="/en/comps/15/EFL-League-One-Seasons">EFL League One</a>, 
        <a href="/en/comps/16/EFL-League-Two-Seasons">EFL League Two</a>, 
        <a href="/en/comps/34/National-League-Seasons">National League</a>
    </td>
</tr>
'''

