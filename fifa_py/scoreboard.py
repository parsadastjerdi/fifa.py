from datetime import datetime

from futbol_py.constants import COUNTRY

TODAY = datetime.today()

class Scoreboard:
    """
        A scoreboard for all games in a given day

        Args:
            :month: Specified month (1-12)
            :day: Specified day (1-31)
            :year: Specified year (YYYY)
            :

        Attributes:
            :json: Contains the full json dump
    """

    def __init__(self, 
                 month=TODAY.month,
                 day=TODAY.day,
                 year=TODAY.year):
        
        self.game_date = None
        self.json = None