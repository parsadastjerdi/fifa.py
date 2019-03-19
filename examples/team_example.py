import sys
sys.path.append('../')

from pprint import pprint

from fifa_py import team
from fifa_py.constants import LEAGUES

tl = team.TeamList(league_id=LEAGUES['EPL']['id'])

pprint(tl.info())
