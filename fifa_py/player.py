from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()
    

class Player:
    '''
        Returns player data
    '''
    def __init__(self):
        pass


class PlayerList:
    '''
        Returns a list of players given
    '''

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
    pass

