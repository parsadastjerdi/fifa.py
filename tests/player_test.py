import unittest
from fifa_py.player import *
from time import sleep


class PlayerTest(unittest.TestCase):
    def setup(self):
        self.pid = get_player(firstname='Lionel', lastname='Messi')
        self.vs_pid = get_player(firstname='Cristiano', lastname='Ronaldo')

    def teardown(self):
        pass

    def testA(self):
        # assert get_player(self.pid)
        assert Player()
        assert PlayerList()
        assert PlayerSummary(pid=self.pid)
        assert PlayerCareer(pid=self.pid)
        assert PlayerProfile(pid=self.pid)
        assert PlayerGameLogs(pid=self.pid)
        assert PlayerVsPlayer(pid=self.pid, vs_pid=self.vs_pid)
        assert TopPlayers(country='us')


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
        self.summary = PlayerSummary(pid=pid)

    def teardown(self):
        pass
    
    def testA(self):
        pass

if __name__ == '__main__':
    unittest.main()
