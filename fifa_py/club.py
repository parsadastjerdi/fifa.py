from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()

class Club:
    '''
        Returns data related to a single club
    '''
    
    def __init__(self, club_id, **kwargs):
        pass

    def info(self, **kwargs):
        pass


class ClubSummary:
    '''
        Returns detailed overview of a club
    '''

    def __init__(self, club_id, **kwargs):
        self.club_id = club_id


