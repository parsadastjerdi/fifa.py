from fifa_py import api_scrape, get_json
from fifa_py import constants

from datetime import datetime

TODAY = datetime.today()

# Notes: need actual endpoint values, current values are just placeholders

# shouldn't this just return a pid for each player
def get_player(first_name, 
                last_name=None, 
                season=constants.CURRENT_SEASON,

                just_id=True, 
                **kwargs):
    '''
    Overview:
        Returns a Player object given a player id
    Input:
    Output:
    '''
    if last_name == None:
        name = first_name.lower() # why even bother doing this?
    else:
        name = '{}, {}'.format(last_name, first_name).lower()

    player = Player()

def get_pid(first_name=None,
            last_name=None,
            season=constants.CURRENT_SEASON,
            **kwargs):
    '''
    Gets a player id for 
    Args:
    Returns:
    Raises:
    '''

    if first_name == None or last_name == None:
        return None
    
    
    

class Player:
    '''
    Overview:
        Returns player data
    Input:
    Output:
    '''

    _endpoint = '/en/players/'

    def __init__(self, pid=None):
        pass


class PlayerList:
    '''
    Overview
        Returns a list of players given a club or something or date, not sure yet
    Input:
    Output:
    '''

    _endpoint = 'playerlist'

    def __init__(self, 
                league,
                season=TODAY.year(), 
                only_current=True, # see if this is necessary or not, also test boolean instead of 1/0
                **kwargs):

        self.json = get_json(self._endpoint, params={'LeagueID': league, 'Season': season, 'IsOnlyCurrentSeason': only_current})

    
    def info(self):
        return api_scrape(self.json, 0)


class PlayerSummary:
    '''
    Overview:
        Returns extended statistics for a specific player
    Input:
    Output:
    '''

    def __init__(self, pid, **kwargs):
        pass


class PlayerCareer:
    '''
    Overview:
        Returns statistics over a players career
    Input:
    Output:
    '''

    def __init__(self, pid, **kwargs):
        pass


class PlayerProfile(PlayerCareer):
    '''
    Overview:
        Returns 
    Input:
    Output:
    '''
    
    def __init__(self, pid, **kwargs):
        pass


class PlayerGameLogs:
    '''
    Overview
    Input:
    Output:
    '''

    def __init__(self, pid, **kwargs):
        pass


class PlayerVsPlayer:
    '''
    Not sure if i want this one yet
    '''

    def __init__(self, pid, vs_pid, **kwargs):
        pass


class TopPlayers():
    '''
    Overview:
        Gets a list of top players for each country from the initial players list
    Input:
    Output:
    '''

    def __init__(self, country, date=TODAY, **kwargs):
        pass

    
