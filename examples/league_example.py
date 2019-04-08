import sys
sys.path.append('../')

from fifa_py.league import League, LeagueList
from fifa_py import _get_key

key = _get_key()

def getLeague(id):
    l = League(league_id=id, api_key=key, include='season')
    info = l.info()
    info.drop(['logo_path', 'coverage', 'live_standings', 'season'], axis=1, inplace=True)
    print(info.T['data'])

    include = l.include()
    print(include.T)
    info.to_csv('csv/league.csv')
    
    include = l.include()
    print(include.T)


def getLeagueList():
    ll = LeagueList(api_key=key, include='season')
    info = ll.info()
    info.drop(['season', 'coverage', 'logo_path', 'season'], axis=1, inplace=True)
    print(info)
    info.to_csv('csv/league_list.csv')


def getLeagueIds():
    ll = LeagueList(api_key=key, include='season')
    info = ll.info()['id']
    print(info)
    info.to_csv('csv/league_ids.csv')


# getLeague(2)
# getLeagueList()
getLeagueIds()

