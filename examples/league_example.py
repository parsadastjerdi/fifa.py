import sys
sys.path.append('../')

from fifa_py.league import League, LeagueList
from fifa_py import _get_key

key = _get_key()

ll = LeagueList(api_key=key)
print(ll.info().T)
