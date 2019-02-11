from fifa_py import api_scrape, get_json
from fifa_py import constants

from datetime import datetime

TODAY = datetime.today()

# Notes: need actual endpoint values, current values are just placeholders

def get_player(pid):
    '''
        Returns a Player object given a player id
    '''
    pass
    

class Player:
    '''
        Returns player data
    '''

    _endpoint = 'players/'

    def __init__(self):
        pass


class PlayerList:
    '''
        Returns a list of players given
    '''

    _endpoint = 'playerlist'

    def __init__(self, **kwarg season=TODAY.year(), **kwarg only_current=1):
        pass

    
    def info(self):
        '''
            Returns the list of players
        '''
        pass


class PlayerSummary:
    '''
        Returns extended statistics for a player
    '''

    _endpoint = 'playersummary'

    pass


class PlayerCareer:
    '''
        Returns statistics over a players career
    '''

    def __init__(self):
        pass


class PlayerProfile(PlayerCareer):
    '''
        Returns 
    '''
    
    def __init__(self):
        pass
