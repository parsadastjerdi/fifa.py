class Livescore:
    '''
    Displays a scoreboard for all games for a given date

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'livescores'
    
    def __init__(self, 
                    api_key, 
                    include, 
                    **kwargs):
        pass


    def available(self):
        pass

    def game_header(self, league=None, **kwargs):
        if league == None:
            # return data for all leagues
            pass
