from fifa_py import player
from time import sleep

def player_test():
    pid = player.get_player('Lionel', 'Messi')
    vs_pid = player.get_player('Cristiano', 'Ronaldo')

    assert player.PlayerList()
    assert player.PlayerSummary(pid)
    assert player.PlayerCareer(pid)
    assert player.PlayerProfile(pid)
    assert player.PlayerGameLogs(pid)
    assert player.PlayerVsPlayer(pid, vs_pid)
