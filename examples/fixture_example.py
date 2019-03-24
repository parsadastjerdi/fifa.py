import sys
sys.path.append('../')

from fifa_py.fixture import Fixture, FixtureList
from fifa_py import _get_key

from pprint import pprint

'''
When doing this yourself, copy and paste your api-key directly into the code itself.
You could also use a similiar method that is used here and store your api key in a seperate file.
ex:
    api_key = '123456789'
'''

api_key = _get_key()

f = Fixture(fixture_id=6361, api_key=api_key, include='stage')
# print(f.info().T)
# print(f.details().T)
# print(f.weather_report().T)
# print(f.scores().T)
# print(f.time().T)
# print(f.coaches().T)
# print(f.standings().T)
# print(f.colors().T)
# scores = f.include()

# fl = FixtureList(api_key=api_key)
# print(fl.info())

