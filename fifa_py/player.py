from fifa_py import api_scrape, get_json, scrape
from fifa_py.constants import COUNTRY

from datetime import datetime

TODAY = datetime.today()


class PlayerNotFoundException(Exception):
    pass


def get_pid(first_name=None,
            last_name=None,
            league_id=None,
            **kwargs):
    '''
    Gets a single player id given a player name
    Args:
        first_name: First name of the desired player
        last_name: Last name of the desired player
        country_id: ID of the country the player plays in
    Returns:
        player_id: an array that contains all player_id's that match that name
        None: If either the first name or the last is None or player couldn't be found
    Raises:
    '''

    if first_name == None or last_name == None:
        return None  
    
    name = '{}-{}'.format(first_name, last_name)
    ids = [0]

    # this should return the specific 
    # country = COUNTRY[country_id]['class']

    if len(ids) == 0:
        raise PlayerNotFoundException

    # json = get_json(endpoint=BASE)
    
    return 'dea698d9'

  

class Player:
    '''
    Returns a player object given a pid
    '''

    # _endpoint = '/en/players/'
    _endpoint = 'players'

    def __init__(self, 
                player_id=None,
                current_season=True,
                **kwargs):
        self.json = get_json(self._endpoint, params={'PlayerID': player_id})
        # returns the entire thing once in the first element and then again in all elements
        # self.json = scrape(endpoint=self._endpoint, params={'PlayerID': player_id + '/Cristiano-Ronaldo'})

    def info(self):
        # return api_scrape(self.json, 0) # check number
        return self.json


class PlayerList:
    '''
    Returns a list of players given a club or something or date, not sure yet
    '''

    _endpoint = 'playerlist'

    def __init__(self,
                league,
                season=TODAY.year, 
                only_current=True, # see if this is necessary or not, also test boolean instead of 1/0
                **kwargs):

        self.json = get_json(self._endpoint, params={'Country': country, 'LeagueID': league, 'Season': season, 'IsOnlyCurrentSeason': only_current})

    
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

    
