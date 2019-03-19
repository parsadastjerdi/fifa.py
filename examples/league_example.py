import sys
sys.path.append('../')

from fifa_py.constants import LEAGUES
from fifa_py.league import League, Standings

from pprint import pprint

l = League(LEAGUES['EPL'])

s = Standings(league_id=LEAGUES['EPL'])
pprint(s.info())
