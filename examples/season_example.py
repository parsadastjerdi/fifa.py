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
    info = s.info()
    # only returns one season??
    return DataFrame(info['results'][1]['data'])


# Note time contains the match date for every match
if __name__ == '__main__':
    seasons = getSeasons()
    seasons.drop(['assistants', 'coaches', 'standings', 'time'], axis=1, inplace=True)
    print(seasons.T)
    seasons['formations'].to_csv('csv/seasons.csv')
    # pprint(seasons['time'])
    # pprint(DataFrame(seasons['scores']).T[0])
    # print(DataFrame(seasons['standings']))
