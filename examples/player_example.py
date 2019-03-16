'''
    This file contains an example of how to use the fifa_py.player module.
'''
import sys
sys.path.append('../')

from fifa_py.player import PlayerList
from fifa_py.constants import LEAGUE

pl = PlayerList(league=LEAGUE['EPL'])
print(pl.json)
