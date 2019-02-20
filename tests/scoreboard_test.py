import unittest
from fifa_py.scoreboard import ScoreBoard
from time import sleep

class ScoreBoardTest(unittest.TestCase):
    def setup(self):
        self.scoreboard = ScoreBoard()
    
    def teardown(self):
        pass

    def testA(self):
        assert self.scoreboard.available()
        # try a general all leagues statement
        assert self.scoreboard.game_header(league='EnglishPremierLeague')
        assert self.scoreboard.game_header(league='Bundesliga')
        assert self.scoreboard.game_header(league='LaLiga')


if __name__ == '__main__':
    unittest.main()