import sys, os
sys.path.append('../')

from fifa_py.player import Player
from fifa_py.team import TeamSquad, TeamList
from fifa_py.season import Season
from fifa_py import _get_key

api_key = _get_key()

# Dropping these features because we don't use them (only have NaN)
# ts.drop(['crosses', 'dribbles', 'duels', 'fouls', 'passes', 'penalties'], axis=1, inplace=True)
def getAllPlayers(output):
    s = Season(api_key=api_key).info()

    for season in s['id']:
        tl = TeamList(season_id=season, api_key=api_key).info()
        print('Season:', season)

        for team in tl['id']:
            print('Retreiving team #' +  str(team) + '...')

            ts = TeamSquad(season_id=season, team_id=team, api_key=api_key).info()

            if ts.empty: 
                print('Team #' + str(team) + ' is empty')
                continue

            if not os.path.isfile(output):
                ts.to_csv(output, header='column_names')
            else:
                ts.to_csv(output, mode='a', header=False)

            print('Team #' + str(team) + ' written to', output)

def test():
    p = Player(api_key=api_key, player_id=4).info()
    print(p['player_id'][0])


if __name__ == '__main__':
    # getAllPlayers('csv/players.csv')
    test()
