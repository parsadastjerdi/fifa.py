import sys
sys.path.append('../')

from fifa_py.season import Season
from fifa_py import _get_key

from pprint import pprint

'''
When doing this yourself, copy and paste your api-key directly into the code itself.
You could also use a similiar method that is used here and store your api key in a seperate file.
ex:
    api_key = '123456789'
'''

api_key = _get_key()

s = Season(season_id=1273, api_key=api_key, include='results')
pprint(s.include())

