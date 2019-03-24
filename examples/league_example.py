import sys
sys.path.append('../')

from fifa_py.league import League, Standings
from fifa_py import _get_key

key = _get_key()

l = League(league_id=,api_key=key)
