from fifa_py import _api_scrape, _get_json, _form_endpoint
from fifa_py.constants import Status

class Player:
    '''
    Returns a player object given a pid
    Args:
    Returns:
    Raises:
    Notes:
        Pass in stats for the init include because most of the time, want stats for the player.
        Avoids having to get resources twice for a common request. 
        The rest of the includes have to be passed individually.
        Also, can't pass in a list of includes and return one large json object due to memory
        constraints.
    '''

    _endpoint = 'players'

    def __init__(self, 
                    player_id,
                    api_key,
                    include=None,
                    **kwargs):
        self._endpoint = _form_endpoint([self._endpoint, player_id])
        self._include = include
        self.json = _get_json(endpoint=self._endpoint, 
                                api_key=self._api_key,
                                include={'include': self._include)

    def info(self):
        return _api_scrape(self.json, 
                            key=['data'], 
                            exclude=None) 

    def include(self):
        return _api_scrape(self.json,
                            key=['data', self._include, 'data'],
                            exclude=None)

    def meta(self):
        return _api_scrape(self.json,
                            key=['meta'],
                            exclude=None) 


class TopPlayers:
    '''
    Overview:
        Gets a list of top players for each country from the initial players list
    Input:
    Output:
    Notes:
        Add stage_id parameter
    '''

    _endpoint = 'topscorers'
    _include = ['goalscorers.player', 'goalscorers.team', 
                'cardscorers.player', 'cardscorers.team', 
                'assistscorers.player', 'assistscorers.team']

    def __init__(self, 
                    season_id, 
                    api_key,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, 'season', season_id])
        self.json = _get_json(endpoint = endpoint, 
                                api_key=api_key,
                                include={'include': self._include})

    def info(self):
        return _api_scrape(self.json, 
                            key=['data'],
                            exclude=['goalscorers', 'cardscorers', 'assistantscorers'])
    
    def goalscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'goalscorers'],
                            exclude=None)   

    def cardscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'cardscorers'],
                            exclude=None)  

    def assistscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'assistantscorers'],
                            exclude=None)      



class AggregratedTopPlayers:
    '''
    Overview:
        Gets a list of top players for each country from the initial players list
    Input:
    Output:
    Notes:
        Add stage_id parameter
    '''

    _endpoint = 'topscorers'
    _include = ['aggregratedGoalscorers.player', 'aggregratedGoalscorers.team', 
                'aggregratedCardscorers.player', 'aggregratedCardscorers.team', 
                'aggregratedAssistscorers.player', 'aggregratedAssistscorers.team']

    def __init__(self, 
                    season_id, 
                    api_key,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, 'season', season_id])
        self.json = _get_json(endpoint = endpoint, 
                                api_key=api_key,
                                include={'include': self._include})

    def info(self):
        return _api_scrape(self.json, 
                            key=['data'],
                            exclude=['aggregratedGoalscorers', 'aggregratedCardscorers', 'aggregratedAssistantscorers'])
    
    def goalscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'aggregratedGoalscorers'],
                            exclude=None)   

    def cardscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'aggregratedCardscorers'],
                            exclude=None)  

    def assistscorers(self):
        return _api_scrape(self.json, 
                            key=['data', 'aggregratedAssistantscorers'],
                            exclude=None)  


# ------------------------------------------------------- #
#               Extra classes                             #
# ------------------------------------------------------- #


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
        self.json = _get_json(endpoint=endpoint)

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
    _include = ['']

    def __init__(self,
                    league_id,
                    api_key,
                    **kwargs):
        endpoint = _form_endpoint([self._endpoint, league_id])
        self.json = _get_json(endpoint=endpoint,
                                api_key=api_key,
                                include=self._include)
    
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


    
