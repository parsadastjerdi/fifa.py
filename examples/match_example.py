import sys
sys.path.append('../')
import json

from pprint import pprint

from fifa_py.match import MatchList
from fifa_py.constants import LEAGUES

m = MatchList(league_ids=LEAGUES['EPL']['id']).info()[2]
pprint(m)
print()
print(m['awayTeam'])
print(m['homeTeam'])
print(m['id'])