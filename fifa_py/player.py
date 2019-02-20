from fifa_py import api_scrape, get_json
from fifa_py import constants

from datetime import datetime

TODAY = datetime.today()

# Notes: need actual endpoint values, current values are just placeholders

def get_player(firstname, lastname, pid=0, **kwargs):
    '''
    Overview:
        Returns a Player object given a player id
    Input:
    Output:
    '''

    return Player(pid)
    

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

    def __init__(self, season=TODAY.year(), only_current=1, **kwargs):
        pass

    
    def info(self):
        '''
        Overview:
            Returns the list of players
        Input:
        Output:
        '''
        pass


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

    
