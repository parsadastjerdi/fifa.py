
# fifa_py
[![Travis](https://img.shields.io/travis/seemethere/nba_py.svg?style=flat-square)](https://travis-ci.org/sports-analytics/fifa_py)   
A Python client for soccer statistics at football-data.org. This client is built on the options available for the free tier of use. In order to use this client you must get your own API key from football-data.org. API Keys are free at the time of writing, but there are paid tiers to allow you to hit the API at a higher rate. 

## Installation
(package isn't uploaded to PyPi yet)
```
pip install fifa_py
```

## Dependencies [![Requires.io](https://img.shields.io/requires/github/sports-analytics/fifa_py.svg?style=flat-square)](https://requires.io/github/sports-analytics/fifa_py/requirements/?branch=master)
- [HTTP Requests](http://www.python-requests.org/en/latest/)
- [Pandas (Optional)](https://pandas.pydata.org/)


## Quickstart
In order to understand how resources are organized at football-data.org, look at their [quickstart page](https://www.football-data.org/documentation/quickstart)

Before using the client, make sure to [register](https://www.football-data.org/client/register) your own API key. After getting your key through email, create a file called .api-key in the root directory of the project and copy your key over into the file. This will allow the scripts to use your key to scrape the database.
