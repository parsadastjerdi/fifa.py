from fifa_py import _api_scrape, _get_json, _form_endpoint

class Season:
    '''
    Returns data related to a single season
    Args:
    Returns:
    Raises:
    Notes:
    '''

    _endpoint = 'seasons'
    
    def __init__(self, 
                season_id, 
                api_key,
                include=None,
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, season_id])
        self._include = include
        self.json = _get_json(endpoint=endpoint, 
                                api_key=api_key,
                                include={'include': self._include})

    def info(self):
        return _api_scrape(json=self.json, 
                            key=['data'], 
                            exclude=None)

    def details(self):
        return _api_scrape(json=self.json, 
                            key=['data'], 
                            exclude=[self._include])   
    
    def meta(self):
        return _api_scrape(json=self.json, 
                            key=['meta'], 
                            exclude=None)
    
    def include(self):
        return _api_scrape(self.json,
                            key=['data', self._include, 'data'],
                            exclude=None)