import sys
sys.path.append('../')

from fifa_py.player import Player
from fifa_py.constants import LEAGUES

from pprint import pprint

pl = Player(player_id=44).info()
pprint(pl)
