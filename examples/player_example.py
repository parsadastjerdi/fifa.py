import sys
sys.path.append('../')
from fifa_py.player import get_pid, Player
pid = get_pid(first_name='Cristiano', last_name='Ronaldo')
player = Player(pid)
player_stats = player.info()


for stat in player.info():
    print(stat, player.info()[stat])


player_stats['Apps']
player_stats['Min']
player_stats['Gls']
player_stats['CrdY']
player_stats['CrdR']
