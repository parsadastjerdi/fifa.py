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

    _endpoint = 'clubsummary'

    def __init__(self, club_id, **kwargs):
        self.club_id = club_id



class ClubDetails:
    '''

    '''

    _endpoint = 'clubdetails'

    def __init__(self, club_id, **kwargs):
        pass


class ClubCommonRoster:
    '''
    '''

    def __init__(self, club_id, **kwargs):
        pass


# add splits if they exist?

class TeamPlayers:
    '''
    '''

    def __init__(self, club_id, **kwargs):
        pass



class ClubLineup:
    '''
    '''

    def __init__(self, club_id, **kwargs):
        pass


class TeamGameLog:
    '''
    '''

    def __init__(self, club_id, **kwargs):
        pass



class ClubSeasons:
    '''
    '''

    def __init__(self, club_id, **kwargs):
        pass