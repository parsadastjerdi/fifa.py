import unittest
from fifa_py.player import get_player, Player, PlayerList, PlayerSummary, PlayerCareer, PlayerProfile, PlayerGameLogs, PlayerVsPlayer, TopPlayers
from time import sleep


class PlayerTest(unittest.TestCase):
    def setup(self):
        self.pid = get_player(firstname='Lionel', lastname='Messi')
        self.vs_pid = get_player(firstname='Cristiano', lastname='Ronaldo')

    def teardown(self):
        pass

    def testA(self):
        assert Player()
        assert PlayerList()
        assert PlayerSummary(pid=self.pid)
        assert PlayerCareer(pid=self.pid)
        assert PlayerProfile(pid=self.pid)
        assert PlayerGameLogs(pid=self.pid)
        assert PlayerVsPlayer(pid=self.pid, vs_pid=self.vs_pid)
        assert TopPlayers(country='esp')


class PlayerListTest(unittest.TestCase):
    def setup(self):
        self.list = PlayerList()

    def teardown(self):
        pass

    def testA(self):
        pass


class PlayerSummaryTest(unittest.TestCase):
    def setup(self):
        pid = get_player(firstname='Lionel', lastname='Messi')
        self.player = PlayerSummary(pid=pid, season=2016)

    def teardown(self):
        pass
    
    def testA(self):
        assert self.player['appearances'] == 34
        assert self.player['starts'] == 32
        assert self.player['subs'] == 2
        assert self.player['minutes'] == 2828
        assert self.player['goals'] == 37
        assert self.player['assists'] == 9
        assert self.player['pk'] == 6
        assert self.player['fouls'] == 15


class PlayerCareerTest(unittest.TestCase):
    def setup(self):
        pid = get_player('Lionel', 'Messi')
        self.player = PlayerCareer(pid)

    def teardown(self):
        pass

    def testA(self):
        pass


class PlayerProfileTest(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def testA(self):
        pass


class PlayerGameLogsTest(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def testA(self):
        pass


class PlayerVsPlayerTest(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def testA(self):
        pass


class TopPlayersTest(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def testA(self):
        pass


if __name__ == '__main__':
    unittest.main()
