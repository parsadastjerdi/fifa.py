import unittest
import sys
sys.path.append('../')

from fifa_py import player
from fifa_py import _get_key

api_key = _get_key()

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.p = player.Player(api_key=api_key, player_id=4, ).info()

    def tearDown(self):
        pass

    def testA(self):
        assert self.p['player_id'][0] == 4
        assert self.p['country_id'][0] == 38
        assert self.p['position_id'][0] == 2
        assert self.p['common_name'][0] == 'J. Kromkamp'
        assert self.p['fullname'][0] == 'Jan Kromkamp'
        assert self.p['firstname'][0] == 'Jan'
        assert self.p['lastname'][0] == 'Kromkamp'
        assert self.p['nationality'][0] == 'Netherlands'
        assert self.p['birthdate'][0] == '17/08/1980'
        assert self.p['birthplace'][0] == 'Makkinga'
        assert self.p['height'][0] == '184 cm'
        assert self.p['weight'][0] == '83 kg'


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
