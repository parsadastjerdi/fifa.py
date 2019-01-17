from datetime import datetime 

_curr_year = datetime.now().year



COUNTRY = {
    'AUS': {
        'name': 'Australia',
        'country_id': 'AUS'

    }, 'AUT': {
        'name': 'Austria',
        'country_id': 'AUT',

    }, 'BEL': {
        'name': 'Belgium'

    }, 'CAN': {
        'name': 'Canada'

    }, 'HRV': {
        'name': 'Croatia'

    }, 'DNK': {
        'name': 'Denmark'

    }, 'GBR': {
        'name': 'England' 

    }, 'ESP': {
        'name': 'Spain'

    }, 'FRA': {
        'name': 'France'

    }, 'DEU': {
        'name': 'Germany'

    }, 'GRC': {
        'name': 'Greece'

    }, 'ITA': {
        'name': 'Italy'

    }, 'LIE': {
        'name': 'Liechtenstein'

    }, 'MEX': {
        'name': 'Mexico'

    }, 'NLD': {
        'name': 'Netherlands'

    }, 'NZL': {
        'name': 'New Zealand'

    }, 'POL': {
        'name': 'Poland'

    }, 'PRT': {
        'name': 'Portugal'

    }, 'PRI': {
        'name': 'Puerto Rico'

    }, 'RUS': {
        'name': 'Russia'

    }, 'SCO': {
        'name': 'Scotland'

    }, 'CHE': {
        'name': 'Switzerland'

    }, 'TUR': {
        'name': 'Turkey'

    }, 'UKR': {
        'name': 'Ukraine'

    }, 'USA': {
        'name': 'United States'

    }
}


class Club:
    def __init_(self, country):
        self.country = country


class League:
    def __init__(self, country):
        self.country = country
