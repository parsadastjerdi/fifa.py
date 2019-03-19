from fifa_py import _get_json,_api_scrape, _form_endpoint
from fifa_py.constants import Standing


class League:
    '''
    Returns a league object
    Args:
        league_id: this id is used to 
    Returns:
    Raises:
    '''

    _endpoint = 'competition'

    def __init__(self, 
                league, 
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, league['code']]) 
        try:       
            self.json = _get_json(endpoint=endpoint, 
                                    filters= {
                                        'league': league['code']
                                    })
        except Exception as e:
            print(e)
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=None,
                            exclude=None)


class LeagueList:
    '''
    Retrieves a list of all available leagues
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'competition'

    def __init__(self):
        self.json = _get_json(endpoint=self._endpoint)
    
    def info(self):
        pass

    
class Standings:
    '''
    '''
    _endpoint = 'competitions'

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

