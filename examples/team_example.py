import sys
sys.path.append('../')

from fifa_py.team import Team, TeamList
from fifa_py.season import Season
from fifa_py import _get_key

from pprint import pprint

api_key = _get_key()


def getSeasons():
    s = Season(api_key=api_key, include='results')
    info = s.info()
    return info['id']


def getTeamList(season):
    t = TeamList(api_key=api_key, season_id=season)
    return t.info()


def getTeam(id):
    t = Team(team_id=id, api_key=api_key)
    info = t.info()
    return info


# Gets data for 8 seasons (0-7). Only 6 has extra data for some reason
def getTeamStats(team_id):
    t = Team(team_id=team_id, api_key=api_key, include='stats')
    include = t.include()
    include.drop(['scoring_minutes'], axis=1, inplace=True)
    return include.T[6]



if __name__ == '__main__':
    tl = getTeamList(5307)
    tl.drop(['logo_path', 'twitter'], axis=1, inplace=True)
    print(tl['id'])

    id = tl['id'][14]
    
    t = Team(team_id=id, api_key=api_key, include='stats')
    print(t.include()['team_id'])

