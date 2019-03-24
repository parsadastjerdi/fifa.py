from fifa_py import _api_scrape, _get_json, _form_endpoint

class Team:
    '''
    Returns data related to a single team

    Args:

    Returns:
        
    '''

    _endpoint = 'teams'
    
    def __init__(self,
                    api_key, 
                    team_id,
                    include=None,
                    by_season=False,
                    **kwargs):
        if by_season:
            self._endpoint = _form_endpoint([self._endpoint, 'season', team_id])
        else:
            self._endpoint = _form_endpoint([self._endpoint, team_id])
            
        self._include = include
        self.json = _get_json(endpoint=self._endpoint,
                                api_key=api_key,
                                include={'include': self._include})

    def info(self):
        return _api_scrape(self.json, 
                            key=['data'], 
                            exclude=None)

    def meta(self):
        return _api_scrape(self.json, 
                            key=['meta'], 
                            exclude=None)   
    def details(self):
        return _api_scrape(self.json,
                            key=None,
                            exclude=[self._include])

    def include(self):
        return _api_scrape(self.json,
                            key=['data', self._include, 'data'],
                            exclude=None)
        


class TeamList:
    '''
    Gives a list of teams for a specific league/competition

    Args:
        league_id (int): valid league id
        season (YYYY): year only 
        stage (enum): Stage enumeration in constants.py

    Returns:
    '''

    _endpoint = 'teams'

    def __init__(self,
                    api_key, 
                    team_id,
                    include=None,
                    by_season=False,
                    **kwargs):
        if by_season:
            self._endpoint = _form_endpoint([self._endpoint, 'season', team_id])
        else:
            self._endpoint = _form_endpoint([self._endpoint, team_id])

        self._include = include
        self.json = _get_json(endpoint=self._endpoint,
                                api_key=api_key,
                                include={'include': self._include})
    
    def info(self):
        return _api_scrape(self.json, 
                            key=['teams'], 
                            exclude=None)
    
    def details(self):
        return _api_scrape(self.json,
                            key=None,
                            exclude=None)

