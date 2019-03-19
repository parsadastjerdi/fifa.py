import sys
sys.path.append('../')

from fifa_py.player import PlayerSummary, Player

from pprint import pprint

'''
In order to get information regarding a single player, you can use either Player or PlayerSummary.
They call different endpoints, but the 
'''
pd = PlayerSummary(player_id=44).info()
print(pd.T)

pl = Player(player_id=44)
print(pl.info())