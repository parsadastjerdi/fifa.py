from fifa_py import _api_scrape, _get_json, _form_endpoint
from fifa_py.constants import CURRENT_SEASON

class Fixture:
    '''
    Returns data related to a single fixture
    How is this different from FixtureSummary
    Args:
    Returns:
    Raises:
    Notes:
    '''

    _endpoint = 'fixtures'
    
    def __init__(self, 
                fixture_id, 
                api_key,
                include=None,
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, fixture_id])
        self._api_key = api_key
        self._include = include
        self.json = _get_json(endpoint=endpoint, 
                                api_key=api_key,
                                include={'include': include})
    
    def info(self):
        return _api_scrape(json=self.json, 
                            key=['data'], 
                            exclude=None)

    def details(self):
        return _api_scrape(json=self.json,
                            key=['data'],
                            exclude=['weather_report', 'formations', 'scores', 'time', 'coaches', 'standings', 'assistants', 'colors'])
    
    def meta(self):
        return _api_scrape(json=self.json,
                            key=['meta'],
                            exclude=None)
    
    def weather_report(self):
        return _api_scrape(json=self.json,
                            key=['data', 'weather_report'],
                            exclude=None)
    
    def scores(self):
        return _api_scrape(json=self.json,
                            key=['data', 'scores'],
                            exclude=None)
    
    def time(self):
        return _api_scrape(json=self.json,
                            key=['data', 'time'],
                            exclude=None)

    def coaches(self):
        return _api_scrape(json=self.json,
                            key=['data', 'coaches'],
                            exclude=None)
    
    def standings(self):
        return _api_scrape(json=self.json,
                            key=['data', 'standings'],
                            exclude=None)

    def colors(self):
        return _api_scrape(json=self.json,
                            key=['data', 'colors'],
                            exclude=None)

    def include(self):
        try:
            return _api_scrape(json=self.json,
                                key=['data', self._include, 'data'],
                                exclude=None)
        except Exception as e:
            print(e)
            return None



class FixtureList:
    '''
    Returns a list of matches, can be more specific given a league or time frame
    
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'seasons'

    def __init__(self, 
                api_key,
                league_id=None,
                matchday=None,
                status=None,
                dateTo=None,
                dateFrom=None,
                **kwargs):
        self._endpoint = _form_endpoint([self._endpoint])
        self._api_key = api_key
        self.json = _get_json(endpoint=self._endpoint,
                                api_key=self._api_key, 
                                include={'include': 'fixtures'})
        

    def info(self):
        return _api_scrape(json=self.json, 
                            key=['data', 'fixtures', 'data'],
                            exclude=None)

    def details(self):
        return _api_scrape(json=self.json,
                            key=['data', 'fixtures', 'data'],
                            exclude=['weather_report', 'formations', 'scores', 'time', 'coaches', 'standings', 
                            'assistants', 'colors'])

    def meta(self):
        return _api_scrape(json=self.json,
                        key=['meta'],
                        exclude=None)


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


class FixtureLineup:
    '''
    Returns the lineup for a specific match

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'fixtures'

    def __init__(self, match_id, **kwargs):
        pass                           