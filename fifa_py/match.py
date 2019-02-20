from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()

class Match:
    '''
    Returns data related to a single match

    Args:
    Returns:
    Raises:
    '''
    
    def __init__(self):
        pass
    
    
    def info(self):
        pass


class MatchList:
    '''
    Returns a list of matches based on a given season
    
    Args:
    Returns:
    Raises:
    '''

    def __init__(self, season=TODAY.year(), **kwargs):
        pass

    def info(self):
        pass


class MatchSummary:
    '''
    Returns a detailed summary of the match

    Args:
    Returns:
    Raises:
    '''

    def __init__(self, match_id, **kwargs):
        pass

    def info(self):
        pass


class MatchLineup:
    '''
    Returns the lineup for a specific match

    Args:
    Returns:
    Raises:
    '''

    def __init__(self, match_id, **kwargs):
        pass