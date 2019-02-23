import unittest
from fifa_py.match import Match, MatchList, MatchSummary, MatchLineup
from time import sleep


class MatchTest(unittest.TestCase):
    def setUp(self):
        match = Match()
    
    def tearDown(self):
        pass
    
    def testA(self):
        pass


class MatchListTest(unittest.TestCase):
    def setUp(self):
        match_list = MatchList()
    
    def tearDown(self):
        pass
    
    def testA(self):
        pass


class MatchSummaryTest(unittest.TestCase):
    def setUp(self):
        match_summary = MatchSummary()
    
    def tearDown(self):
        pass
    
    def testA(self):
        pass


class MatchLineupTest(unittest.TestCase):
    def setUp(self):
        match_lineup = MatchLineup()
    
    def tearDown(self):
        pass

    def testA(self):
        pass


if __name__ == '__main__':
    unittest.main()