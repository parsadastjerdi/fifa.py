import sys
sys.path.append('../')

from fifa_py.team import Team

from fifa_py import _get_key

api_key = _get_key()

def getTeam(id):
    t = Team(team_id=id, api_key=api_key)
    info = t.info()
    return info


def getTeamStats(team_id):
    t = Team(team_id=team_id, api_key=api_key, include='stats')
    # Gets data for 8 seasons (0-7). Only 6 has extra data for some reason
    include = t.include()
    data = include.T[6]
    # data.drop(['scoring_minutes'], axis=1, inplace=True)
    # data.to_csv('csv/teams.csv')
    pprint(data)


def getTeamBySeason(season):
    pass

def getLeagueList():
    ll = LeagueList(api_key=key, include='season')
    info = ll.info()
    info.drop(['season', 'coverage', 'logo_path', 'season'], axis=1, inplace=True)
    return info


if __name__ == '__main__':
    leagues = getLeagueList()
