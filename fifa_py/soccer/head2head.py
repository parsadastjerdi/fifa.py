from fifa_py import _api_scrape, _get_json, _form_endpoint

class Head2Head:
    '''
    Returns data related to a single match
    Args:
    Returns:
    Raises:
    '''
    _endpoint = 'matches'
    
    def __init__(self, 
                match_id, 
                api_key=None,
                include=None,
                **kwargs):
        self._endpoint = _form_endpoint([self._endpoint, match_id])
        self._api_key = api_key
        self._include = include
        self.json = _get_json(endpoint=self._endpoint,
                                api_key=api_key,
                                include={'include': self._include})
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=['head2head'], 
                            exclude=['homeTeam', 'awayTeam'])

    def hometeam(self):
        return _api_scrape(self.json,
                            key=['homeTeam'],
                            exclude=None)
    
    def awayteam(self):
        return _api_scrape(self.json,
                            key=['awayTeam'],
                            exclude=None)
