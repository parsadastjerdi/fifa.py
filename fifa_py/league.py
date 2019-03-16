from fifa_py import _get_json,_api_scrape, _form_endpoint
from fifa_py.constants import CURRENT_SEASON, LEAGUES

class LeagueNotFoundException(Exception):
    pass

class League:
    '''
    Returns a league object
    Args:
        league_id: this id is used to 
    Returns:
    Raises:
    '''

    _endpoint = 'competition'

    def __init__(self, league, **kwargs):
        endpoint = _form_endpoint([self._endpoint, league['code']]) 
        try:       
            self.json = _get_json(endpoint=endpoint, 
                                    filters= {
                                        'league': league['code']
                                    })
        except Exception as e:
            print(e)
    
    def info(self):
        return _api_scrape(self.json)


class LeagueList:
    '''
    Retrieves a list of all available leagues
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'competition'

    def __init__(self):
        pass
    
    def info(self):
        pass


if __name__ == '__main__':
    l = League(LEAGUES['EPL'])
