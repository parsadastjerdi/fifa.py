
# fifa_py
[![Travis](https://img.shields.io/travis/seemethere/nba_py.svg?style=flat-square)](https://travis-ci.org/sports-analytics/fifa_py)   
fifa_py is a Python client for soccer statistics at football-data.org. All football data is provided by the football-data.org API. In order to use this client you must get your own API key. There are multiple paid tiers, as well as a free tier for which you can test out the API.

## Installation
```
pip install fifa_py
```

## Dependencies [![Requires.io](https://img.shields.io/requires/github/sports-analytics/fifa_py.svg?style=flat-square)](https://requires.io/github/sports-analytics/fifa_py/requirements/?branch=master)
- [HTTP Requests](http://www.python-requests.org/en/latest/)
- [Pandas](https://pandas.pydata.org/)


## Quickstart
In order to understand how resources are organized at football-data.org, look at their [quickstart page](https://www.football-data.org/documentation/quickstart)

Before using the client, make sure to [register](https://www.football-data.org/client/register) your own API key. After getting your key through email, create a file called .api-key in the root directory of the project and copy your key over into the file. This will allow the scripts to use your key to scrape the database.
