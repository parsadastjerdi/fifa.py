from fifa_py import api_scrape, get_json
from datetime import datetime

TODAY = datetime.today()

class Club:
    '''
        Returns data related to a single club
    '''
    
    def __init__(self):
        pass

    def info(self):
        pass

class ClubSummary:
    '''
        Returns detailed overview of a club
    '''

    def __init__(self, club_id):
        self.club_id = club_id


