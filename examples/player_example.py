import sys
sys.path.append('../')

from fifa_py.player import Player, TopPlayers, AggregratedTopPlayers

from pprint import pprint

'''
In order to get information regarding a single player, you can use either Player or PlayerSummary.
They call different endpoints, but the 
'''

key = 'i3xpyjjLbwTxssZBtXTml2Gee2cL5fCpvPncKcrcv7Lnc7FzMWm1CZXDocm8'

'''
pl = Player(player_id=92276, api_key=key)
print(pl.info().T)
# print(pl.info()['player_id'][0])

tp = TopPlayers(season_id=12963, api_key=key)
print(tp.goalscorers())
print(tp.goalscorers().columns.tolist())
'''

'''
atp = AggregratedTopPlayers(season_id=12963, api_key=key)
print(atp.goalscorers())
'''