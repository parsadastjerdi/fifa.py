from fifa_py import api_scrape, get_json
from fifa_py import constants

from datetime import datetime

TODAY = datetime.today()


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

    pass

    if first_name == None or last_name == None:
        return None     
  

class Player:
    '''
    Player object
    '''

    # _endpoint = '/en/players/'
    _endpoint = 'players'

    def __init__(self, player_id=None):
        self.json = get_json(self._endpoint, params={'PlayerID': player_id})


    def info(self):
        return api_scrape(self.json, 0) # check number 



class PlayerList:
    '''
    Returns a list of players given a club or something or date, not sure yet
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
    Returns extended statistics for a specific player
    Difference between this and player profile?
    '''

    _endpoint = 'playersummary'

    def __init__(self, player_id, **kwargs):
        pass


class PlayerCareer:
    '''
    Returns all statistics for a player over his career
    '''

    _endpoint = 'playercareer'

    def __init__(self, player_id, **kwargs):
        pass


class PlayerProfile(PlayerCareer):
    '''
    Returns a brief profile of a player (aggregrated statistics over his career)
    Is this necessary or just create a profile() method in PlayerCareer?
    probably better to stick with this to keep everything uniform
    '''

    _endpoint = 'playerprofile'
    
    def __init__(self, player_id, **kwargs):
        pass


class PlayerGameLogs:
    '''
    Returns the game log for a single player
    '''

    def __init__(self, player_id, **kwargs):
        pass


class PlayerVsPlayer:
    '''
    Not sure if i want this one yet
    '''

    def __init__(self, player_id, vs_player_id, **kwargs):
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

    
