from fifa_py.match import MatchList, MatchSummary
from time import sleep

ml = MatchList(season=2016)

for match in ml.info():
    ms = MatchSummary(match['MATCH_ID'])
    # download to csv
