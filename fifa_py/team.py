from fifa_py import _api_scrape, _get_json, _form_endpoint

class Team:
    '''
        Returns data related to a single team
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
        return _api_scrape(json=self.json, key=None, exclude=['area', 'squad', 'activeCompetitions'])
    
    def area(self):
        return _api_scrape(json=self.json, key='area', exclude=None)
    
    def squad(self):
        return _api_scrape(json=self.json, key='squad', exclude=None)

    def active_competitions(self):
        return _api_scrape(json=self.json, key='activeCompetitions', exclude=None)



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
        return _api_scrape(self.json, key='teams', exclude=None)



# ----------------- Not sure if any of the below are necessary ---------------- #
class TeamDetails:
    '''
    Returns club details

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubdetails'

    def __init__(self, club_id, **kwargs):
        pass


class TeamRoster:
    '''
    Returns the common roster of the club 
    
    Args:
    Returns:
    Raises:

    '''

    _endpoint = 'clubcommonroster'

    def __init__(self, club_id, **kwargs):
        pass


# add splits if they exist?

class TeamPlayers:
    '''
    Returns all the players for a given club

    Args:
    Returns:
    Raises:

    '''

    _endpoint = 'clubplayers'

    def __init__(self, club_id, **kwargs):
        pass


class TeamLineup:
    '''
    Returns the lineup of a club for a specific season

    Args:
    Returns:
    Raises:

    '''
    
    _endpoint = 'clublineup'

    def __init__(self, club_id, game_id, **kwargs):
        pass


class TeamGameLog:
    '''
    Returns the game log for a specific club for a specific game

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubgamelog'

    def __init__(self, club_id, **kwargs):
        pass



class TeamSeasons:
    '''
    Returns sum total for a club for a certain season

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubseasons'

    def __init__(self, club_id, **kwargs):
        pass