from fifa_py.player import PlayerList, PlayerSummary
from time import sleep

statslist = ['FIRST_NAME', 'LAST_NAME', 'GOALS_SCORED']

pl = PlayerList(season=2016, only_current=0)

for player in pl.info():
    ps = PlayerSummary(player['PERSON_ID'])

    for stat in statslist:
        # write to csv
        pass



