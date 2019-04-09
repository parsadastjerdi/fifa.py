import sys
sys.path.append('../')

from fifa_py.season import Season
from fifa_py import _get_key

from pprint import pprint

from pandas import DataFrame

api_key = _get_key()

# id = 1273
def getSeasons():
    s = Season(api_key=api_key, include='results')
    s.drop(['assistants', 'coaches'], axis=1, inplace=True)
    info = DataFrame(s.info()['results'][0]['data'])
    return info

if __name__ == '__main__':
    seasons = getSeasons()
    print(seasons.T)



