import sys
sys.path.append('../')

from fifa_py.player import Player, TopPlayers, AggregratedTopPlayers
from fifa_py import get_key

key = get_key()
print('api-key:', key)

# This creates a player object given a specific player id and an api_key 
p = Player(player_id=6389, api_key=key)

print('Stats')
print(p.stats())
print()

print('Position Information')
print(p.position())
print()

print('Team Information')
print(p.team())
print()

print('Trophies Information')
print(p.trophies())
print()

print('Sidelined Information')
print(p.sidelined())
print()

print('Transfers Information')
print(p.transfers())
print()