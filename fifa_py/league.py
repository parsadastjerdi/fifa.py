from fifa_py import _get_json,_api_scrape, _form_endpoint
from fifa_py.constants import Standing


class League:
    '''
    Returns a league object
    Args:
        league_id: 
    Returns:
    Raises:
    Notes:
        Letting country be the default include for this one
    '''

    _endpoint = 'leagues'

    def __init__(self, 
                league_id,
                api_key,
                include=None, 
                **kwargs):
        self._endpoint = _form_endpoint([self._endpoint, league_id]) 
        self._include = include
        self.json = _get_json(endpoint=self._endpoint, 
                                api_key=api_key,
                                include={'include': [self._include]})
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=['data'],
                            exclude=None)
    
    def meta(self):
        return _api_scrape(self.json,
                            key=['meta'],
                            exclude=None)
    
    def include(self):
        return _api_scrape(self.json, 
                            key=['data', self._include, 'data'],
                            exclude=None)


class LeagueList:
    '''
    Retrieves a list of all available leagues
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'leagues'

    def __init__(self,
                    api_key,
                    include=None,
                    **kwargs):
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
    
    
    def include(self):
        print("Data Formatting messes LeagueList.include() up, season included in each league")
        return None
        return _api_scrape(self.json, 
                            key=['data', self._include, 'data'],
                            exclude=None)    
    
    
class Standings:
    '''
    '''
    _endpoint = 'standings'

    def __init__(self, 
                league_id, 
                season=None, 
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, league_id, 'standings'])
        self.json = _get_json(endpoint=endpoint,
                                filters={
                                    'standingType': Standing.home,
                                    'season': season
                                })
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=['standings'],
                            exclude=None)

