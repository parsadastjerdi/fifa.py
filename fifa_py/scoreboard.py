from datetime import datetime

from fifa_py.constants import COUNTRY
from fifa_py.constants import League

TODAY = datetime.today()

class Scoreboard:
    '''
    Displays a scoreboard for all games for a given date
    '''
    def __init__(self, date=TODAY, **kwargs):
        pass


    def available(self):
        '''
        Gives the available statistics for that day
        '''
        pass

    def game_header(self, league=None, **kwargs):
        if league == None:
            # return data for all leagues
            pass