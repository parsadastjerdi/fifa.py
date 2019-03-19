from fifa_py import _api_scrape, _get_json, _form_endpoint 
from fifa_py.constants import Status

class Player:
    '''
    Returns a player object given a pid
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'players'

    def __init__(self, 
                    player_id,
                    status=Status.finished,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, player_id, 'matches'])
        self.json = _get_json(endpoint)

    def info(self):
        return _api_scrape(self.json, 
                            key=None, 
                            exclude=['matches', 'count', 'filters'])
    
    def matches(self):
        return _api_scrape(self.json,
                            key=['matches'],
                            exclude=None)
    
    def _count(self):
        return _api_scrape(self.json,
                            key=['count'],
                            exclude=None)
    
    def filters(self):
        return _api_scrape(self.json,
                            key=['filters'],
                            exclude=None)


class PlayerSummary:
    '''
    Retreived only the specific details for a player, does not give match information
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'players'

    def __init__(self,
                    player_id,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, player_id])
        self.json = _get_json(endpoint)

    def info(self):
        return _api_scrape(self.json, 
                            key=None,
                            exclude=None)

class Scorers:
    '''
    Returns a list of players who scored in a specific league (competition)
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'competitions'

    def __init__(self,
                    league_id,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, league_id])
        self.json = _get_json(endpoint=endpoint)
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=None,
                            exclude=None) 


class PlayerList:
    '''
    Returns a list of players given a club or something or date, not sure yet
    Args:
    Returns:
    Raises:
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
        return _api_scrape(json=self.json, 
                            key=['player'],
                            exclude=None)


# ------------------------------------------------------- #
#               Extra classes                             #
# ------------------------------------------------------- #

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

    def __init__(self, country, **kwargs):
        pass

    
