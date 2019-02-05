from datetime import datetime 

_curr_year = datetime.now().year



COUNTRY = {
    'AUS': {
        'name': 'Australia',
        'id': 'AUS'

    }, 'AUT': {
        'name': 'Austria',
        'id': 'AUT'

    }, 'BEL': {
        'name': 'Belgium',
        'id': 'BEL'

    }, 'CAN': {
        'name': 'Canada',
        'id': 'CAN'

    }, 'HRV': {
        'name': 'Croatia',
        'id': 'HRV'

    }, 'DNK': {
        'name': 'Denmark',
        'id': 'DNK'

    }, 'GBR': {
        'name': 'England',
        'id': 'GBR'

    }, 'ESP': {
        'name': 'Spain',
        'id': 'ESP'

    }, 'FRA': {
        'name': 'France',
        'id': 'FRA'

    }, 'DEU': {
        'name': 'Germany',
        'id': 'DEU'

    }, 'GRC': {
        'name': 'Greece',
        'id': 'GRC'

    }, 'ITA': {
        'name': 'Italy',
        'id': 'ITA'

    }, 'LIE': {
        'name': 'Liechtenstein',
        'id': 'LIE'

    }, 'MEX': {
        'name': 'Mexico',
        'id': 'MEX'

    }, 'NLD': {
        'name': 'Netherlands',
        'id': 'NLD'

    }, 'NZL': {
        'name': 'New Zealand',
        'id': 'NZL'

    }, 'POL': {
        'name': 'Poland',
        'id': 'POL'

    }, 'PRT': {
        'name': 'Portugal',
        'id': 'PRT'

    }, 'PRI': {
        'name': 'Puerto Rico',
        'id': 'PRI'

    }, 'RUS': {
        'name': 'Russia',
        'id': 'RUS'

    }, 'SCO': {
        'name': 'Scotland',
        'id': 'SCO'

    }, 'CHE': {
        'name': 'Switzerland',
        'id': 'CHE'

    }, 'TUR': {
        'name': 'Turkey',
        'id': 'TUR'

    }, 'UKR': {
        'name': 'Ukraine',
        'id': 'UKR'

    }, 'USA': {
        'name': 'United States',
        'id': 'USA'
    }
}


class Club:
    def __init_(self, country):
        self.country = country


class League:
    def __init__(self, country):
        self.country = country
