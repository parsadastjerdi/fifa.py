from fifa_py import get_json, api_scrape
from datetime import datetime

TODAY = datetime.today()

# import information for all countries
from constants import COUNTRY

def get_leagues(country, **kwargs):
    '''
    Returns all leagues within a certain country
    '''
    pass

class League:
    '''
    Returns a league object
    Input:
    Output:
    '''

    def __init__(self, 
                country, 
                league_id,
                **kwargs):
                
        self.country = country
        self.league_id = league_id
