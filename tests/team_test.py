import sys
sys.path.append('../')

import unittest
from time import sleep
from fifa_py.team import Team, TeamList
from fifa_py import _get_key

class TeamTest(unittest.TestCase):
    def setUp(self):
        self.key = _get_key()
    
    def tearDown(self):
        pass

    def core(self):
        t = Team(team_id=53, api_key=self.key)
        info = t.info()
        assert info['id'] == 53
        assert info['legacy_id'] == 152
        assert info['name'] == 'Celtic'
        assert info['short_code'] == 'CEL'
        assert info['venue_id'] == 8909
        assert info['current_season_id'] == 12963
    
        details = t.details()
        assert details['id'] == 0

        include = t.include()
        assert include['id'] == 0
    
    def country(self):
        t = Team(team_id=273, api_key=self.key, include='country')
        info = t.info()

        assert info['id'] == 1161
        assert info['name'] == 'Scotland'
        assert info['extra']['continent'] == 'Europe'
        assert info['extra']['sub_region'] == 'Northern Europe'
        assert info['extra']['world_region'] == 'EMEA'
        assert info['extra']['fifa'] == 'ENG,NIR,SCO,WAL'


    def squad(self):
        t = Team(team_id=53, api_key=self.key, include='squad')

    def coach(self):
        t = Team(team_id=53, api_key=self.key, include='coach') 

    def transfers(self):
        t = Team(team_id=53, api_key=self.key, include='transfers')  

    def sidelined(self):
        t = Team(team_id=53, api_key=self.key, include='sidelined')  
    
    def stats(self):
        t = Team(team_id=53, api_key=self.key, include='stats')
    
    def venue(self):
        t = Team(team_id=53, api_key=self.key, include='venue')
    
    def fifaranking(self):
        t = Team(team_id=53, api_key=self.key, include='fifaranking')
    
    def uefaranking(self):
        t = Team(team_id=53, api_key=self.key, include='uefaranking')
    
    def visitorFixtures(self):
        t = Team(team_id=53, api_key=self.key, include='visitorFixtures')

    def localFixtures(self):
        t = Team(team_id=53, api_key=self.key, include='localFixtures')
    
    def visitorResults(self):
        t = Team(team_id=53, api_key=self.key, include='visitorResults')
    
    def latest(self):
        t = Team(team_id=53, api_key=self.key, include='latest')
    
    def upcoming(self):
        t = Team(team_id=53, api_key=self.key, include='upcoming')
    
    def goalscorers(self):
        t = Team(team_id=53, api_key=self.key, include='goalscorers')

    def cardscorers(self):
        t = Team(team_id=53, api_key=self.key, include='cardscorers')

    def assistscorers(self):
        t = Team(team_id=53, api_key=self.key, include='assistscorers')

    def aggregratedGoalScorers(self):
        t = Team(team_id=53, api_key=self.key, include='aggregratedGoalscorers')
    
    def aggregratedCardScorers(self):
        t = Team(team_id=53, api_key=self.key, include='aggregratedCardscorers')

    def aggregratedAssistScorers(self):
        t = Team(team_id=53, api_key=self.key, include='aggregratedAssistscorers')
        


class TeamListTest(unittest.TestCase):
    def setUp(self):
        self.key = _get_key()
        self.tl = TeamList(team_id=53, api_key=self.key)
    
    def tearDown(self):
        pass
    
    def testA(self):
        pass

    def testIncludes(self):
        pass


if __name__ == '__main__':
    unittest.main()