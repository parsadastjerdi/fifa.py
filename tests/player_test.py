import unittest
import sys
sys.path.append('../')

from fifa_py import player
from fifa_py import _get_key

api_key = _get_key()

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.p = player.Player(api_key=api_key, player_id=4, ).info()
        print(self.p.T)

    def tearDown(self):
        pass

    def testA(self):
        assert self.p['player_id'] == 4
        assert self.p['country_id'] == 38
        assert self.p['position_id'] == 2
        assert self.p['common_name'] == 'J. Kronkamp'
        assert self.p['fullname'] == 'Jan Kromkamp'
        assert self.p['firstname'] == 'Jan'
        assert self.p['lastname'] == 'Kromkamp'
        assert self.p['nationality'] == 'Netherlands'
        assert self.p['birthdate'] == '17/08/1980'
        assert self.p['birthplace'] == 'Makkinga'
        assert self.p['height'] == '184 cm'
        assert self.p['weight'] == '83 kg'


class PlayerListTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerSummaryTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testA(self):
        pass


class PlayerCareerTest(unittest.TestCase):
    def setUp(self):
        pass

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
