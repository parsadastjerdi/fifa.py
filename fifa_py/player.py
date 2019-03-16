from fifa_py import _api_scrape, _get_json, _form_endpoint
from fifa_py.constants import LEAGUES, CURRENT_SEASON

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

    _endpoint = 'players'

    def __init__(self, 
                player_id,
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, player_id])
        self.json = _get_json(endpoint)

    def info(self):
        return _api_scrape(self.json, key=None)


class PlayerList:
    '''
    Returns a list of players given a club or something or date, not sure yet
    '''

    _endpoint = 'players'

    def __init__(self,
                player_id, # player id is necessary .. ?
                season=None,

                **kwargs):
        endpoint = _form_endpoint(self._endpoint)
        self.json = _get_json(endpoint=endpoint, 
                                filters={'competition': league['competition'],
                                        'season': season,
                                        'category': league['category'][2]})
    
    def info(self):
        return _api_scrape(json=self.json, key='player')


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

    
