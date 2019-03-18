from fifa_py import _api_scrape, _get_json, _form_endpoint

class Team:
    '''
    Returns data related to a single team
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'teams'
    
    def __init__(self, 
                team_id, 
                season=None,
                **kwargs):
        endpoint = _form_endpoint([self._endpoint, team_id])
        self.json = _get_json(endpoint=endpoint, 
                                filters = {'season': season})

    def info(self):
        return _api_scrape(json=self.json, 
                            key=None, 
                            exclude=['area', 'squad', 'activeCompetitions'])
    
    def area(self):
        return _api_scrape(json=self.json, 
                            key=['area'], 
                            exclude=None)

    def squad(self):
        return _api_scrape(json=self.json, 
                            key=['squad'], 
                            exclude=None)

    def active_competitions(self):
        return _api_scrape(json=self.json, 
                            key=['activeCompetitions'], 
                            exclude=None)


class TeamList:
    '''
    Gives a list of teams for a specific league/competition
    Args:
    Returns:
    Raises
    '''

    _endpoint = 'competitions/{id}/teams'

    def __init__(self,
                    league_id,
                    **kwargs):
        self.json = _get_json(self._endpoint.format(id=league_id))
    
    def info(self):
        return _api_scrape(self.json, 
                            key='teams', 
                            exclude=None)
    
    def temp(self):
        return _api_scrape(self.json,
                            key=None,
                            exclude=None)

