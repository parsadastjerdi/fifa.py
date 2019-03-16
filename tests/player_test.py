import unittest
from time import sleep
from fifa_py import player
from fifa_py.constants import LEAGUE


class GetPIDTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testA(self):
        assert player.get_pid('Lionel', 'Messi')
        assert player.get_pid('Cristiano', 'Ronaldo')


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.pid = player.get_pid(first_name='Lionel', last_name='Messi')
        self.vs_pid = player.get_pid(first_name='Cristiano', last_name='Ronaldo')

    def tearDown(self):
        pass

    def testA(self):
        assert player.Player(player_id=self.pid)
        assert player.PlayerList(league=LEAGUE['EPL'])
        assert player.PlayerSummary(player_id=self.pid)
        assert player.PlayerCareer(player_id=self.pid)
        assert player.PlayerProfile(player_id=self.pid)
        assert player.PlayerGameLogs(player_id=self.pid)
        assert player.PlayerVsPlayer(player_id=self.pid, vs_player_id=self.vs_pid)
        assert player.TopPlayers(country='esp')


class PlayerListTest(unittest.TestCase):
    def setUp(self):
        self.list = player.PlayerList()

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerSummaryTest(unittest.TestCase):
    def setUp(self):
        pid = player.get_player(first_name='Lionel', last_name='Messi')
        self.plyr = player.PlayerSummary(player_id=pid, season=2016)

    def tearDown(self):
        pass
    
    def testA(self):
        assert self.plyr['appearances'] == 34
        assert self.plyr['starts'] == 32
        assert self.plyr['subs'] == 2
        assert self.plyr['minutes'] == 2828
        assert self.plyr['goals'] == 37
        assert self.plyr['assists'] == 9
        assert self.plyr['pk'] == 6
        assert self.plyr['fouls'] == 15


class PlayerCareerTest(unittest.TestCase):
    def setUp(self):
        pid = player.get_player('Lionel', 'Messi')
        self.player = player.PlayerCareer(pid)

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerProfileTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerGameLogsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerVsPlayerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class TopPlayersTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


if __name__ == '__main__':
    unittest.main()
