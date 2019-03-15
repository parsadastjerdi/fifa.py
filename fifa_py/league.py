from fifa_py import get_json, api_scrape
from datetime import datetime

TODAY = datetime.today()

from fifa_py.constants import LEAGUE

class LeagueNotFoundException(Exception):
    pass

def get_league(league_id=None, **kwargs):
    '''
    Returns all leagues within a certain country
    Args:
    Returns:
    Raises:
    '''
    if league_id is None:
        raise LeagueNotFoundException
    

class League:
    '''
    Returns a league object
    Args:
    Returns:
    Raises:
    '''

    def __init__(self, 
                country, 
                league_id,
                **kwargs):
                
        self.country = country
        self.league_id = league_id
