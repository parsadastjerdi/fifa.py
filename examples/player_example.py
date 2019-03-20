import sys
sys.path.append('../')

from fifa_py.player import Player, TopPlayers, AggregratedTopPlayers
from fifa_py import get_key
from pprint import pprint

'''
In order to get information regarding a single player, you can use either Player or PlayerSummary.
They call different endpoints, but the 
'''

key = get_key()
print('api-key:', key)
p = Player(player_id=6389, api_key=key)
print(p.info()['fullname'])
teams = p.stats()['team_id']
pprint(teams)
pprint(p.json.keys)
# pprint(p.meta())


'''
tp = TopPlayers(season_id=12963, api_key=key)
print(tp.goalscorers())
print(tp.goalscorers().columns.tolist())
'''

'''
atp = AggregratedTopPlayers(season_id=12963, api_key=key)
print(atp.goalscorers())
'''