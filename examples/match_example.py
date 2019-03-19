import sys
sys.path.append('../')
import json

from fifa_py.match import MatchList, Match

m = Match(match_id=246389)
print(m.referees())
print('head2head:')
print(m.head2head().T)
