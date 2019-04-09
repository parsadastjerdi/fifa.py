import sys
sys.path.append('../')

from fifa_py.league import League, LeagueList
from fifa_py import _get_key

key = _get_key()

def getLeague(id):
    l = League(league_id=id, api_key=key, include='season')
    info = l.info()
    info.drop(['logo_path', 'coverage', 'live_standings', 'season'], axis=1, inplace=True)
    return info


def getLeagueList():
    ll = LeagueList(api_key=key, include='season')
    info = ll.info()
    info.drop(['season', 'coverage', 'logo_path', 'season'], axis=1, inplace=True)
    return info


if __name__ == '__main__':
    leagues = getLeagueList()
    leagues.to_csv('csv/leagues.csv')
    print('All available league information saved under csv/leagues.csv')

