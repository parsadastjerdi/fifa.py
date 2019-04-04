import sys
sys.path.append('../')

from fifa_py.player import Player
from fifa_py import _get_key

key = _get_key()
print('api-key:', key)

# This creates a player object given a specific player id and an api_key 
p = Player(player_id=6389, api_key=key, include='stats').include()
print(p.T)

p.to_csv('csv/players.csv')