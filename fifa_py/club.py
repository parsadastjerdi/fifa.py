from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()


class Club:
    '''
        Returns data related to a single club
    '''

    _endpoint = 'club'
    
    def __init__(self, club_id, **kwargs):
        pass

    def info(self, **kwargs):
        pass


class ClubSummary:
    '''
        Returns detailed overview of a club
    '''

    _endpoint = 'clubsummary'

    def __init__(self, club_id, **kwargs):
        self.club_id = club_id



class ClubDetails:
    '''
    Returns club details

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubdetails'

    def __init__(self, club_id, **kwargs):
        pass


class ClubCommonRoster:
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

class ClubPlayers:
    '''
    Returns all the players for a given club

    Args:
    Returns:
    Raises:

    '''

    _endpoint = 'clubplayers'

    def __init__(self, club_id, **kwargs):
        pass


class ClubLineup:
    '''
    Returns the lineup of a club for a specific season

    Args:
    Returns:
    Raises:

    '''
    
    _endpoint = 'clublineup'

    def __init__(self, club_id, game_id, **kwargs):
        pass


class ClubGameLog:
    '''
    Returns the game log for a specific club for a specific game

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubgamelog'

    def __init__(self, club_id, **kwargs):
        pass



class ClubSeasons:
    '''
    Returns sum total for a club for a certain season

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'clubseasons'

    def __init__(self, club_id, **kwargs):
        pass