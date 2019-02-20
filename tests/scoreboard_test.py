import unittest
from fifa_py.scoreboard import ScoreBoard
from time import sleep

class ScoreBoardTest(unittest.TestCase):
    def setUp(self):
        self.scoreboard = ScoreBoard()
    
    def tearDown(self):
        pass

    def testA(self):
        assert self.scoreboard.available()
        assert self.scoreboard.game_header(league='EnglishPremierLeague')
        assert self.scoreboard.game_header(league='Bundesliga')
        assert self.scoreboard.game_header(league='LaLiga')


if __name__ == '__main__':
    unittest.main()