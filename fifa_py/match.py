from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()


class Match:
    '''
        Returns data related to a single match
    '''
    
    def __init__(self):
        pass
    
    
    def info(self):
        pass


class MatchList:
    '''
        Returns a list of matches based on a given season
    '''

    def __init__(self, **kwargs season=TODAY.year()):
        pass

    def info(self):
        pass


class MatchSummary:
    '''
        Returns a detailed summary of the match
    '''

    def __init__(self, **kwargs match_id):
        pass

    def info(self):
        pass