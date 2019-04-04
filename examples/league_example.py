import sys
sys.path.append('../')

from fifa_py.league import League, LeagueList
from fifa_py import _get_key

key = _get_key()

def getLeague(id):
    l = League(league_id=id, api_key=key, include='season')
    info = l.info()
    info.drop(['logo_path'], axis=1)
    # print(info.T)
    # info.to_csv('csv/league.csv')
    include = l.include()
    print(include.T)


def getLeagueList():
    ll = LeagueList(api_key=key, include='season')
    info = ll.info()
    info = info.drop(columns=['season'])
    print(info)
    info.to_csv('csv/league_list.csv')


# getLeague(2)
getLeagueList()
