from datetime import datetime
from enum import Enum

_curr_year = datetime.now().year
if datetime.now().month > 6:
    CURRENT_SEASON = str(_curr_year)
else:
    CURRENT_SEASON = str(_curr_year - 1)


def date(day, month, year, **kwargs):
    '''
    Returns correctly formatted date
    '''
    return year + '-' + month + '-' + day


LEAGUES = {
    'EPL': {
        'name': 'Premier League',
        'alt-name': 'Premier League',
        'country': 'England',
        'code': 'PL',
        'id': 2021

    }, 'LLA': {
        'name': 'Primera Division',
        'alt-name': 'La Liga Santader',
        'code': 'PD',
        'id': 2014
        
    }, 'BSA': {
        'name': 'Serie A',
        'alt-name': 'Serie A',
        'country': 'Brazil',
        'code': 'BSA',
        'id': 2013

    }, 'BUN': {
        'name': 'Bundesliga',
        'alt-name': 'Bundesliga',
        'country': 'Germany',
        'code': 'BL1',
        'id': 2002

    }, 'ENC': {
        'name': 'Championship',
        'alt-name': 'Championship',
        'country': 'England',
        'code': 'ELC',
        'id': 2016

    }, 'ISA': {
        'name': 'Serie A',
        'alt-name': 'Serie A',
        'country': 'Italy',
        'code': 'SA',
        'id':  2019

    }, 'UCL': {
        'name': 'UEFA Champions League',
        'alt-name': 'UEFA Champions League',
        'country': None,
        'code': 'CL',
        'id': 2001

    }, 'EUC': {
        'name': 'European Championship',
        'alt-name': 'European Championship',
        'country': None,
        'code': 'EC',
        'id': 2018

    }, 'LGO': {
        'name': 'Ligue 1', 
        'alt-name': 'Ligue 1',
        'country': 'France',
        'code': 'FL1',
        'id': 2015

    }, 'PPL': {
        'name': 'Primeira Liga',
        'alt-name': 'Primeira Liga',
        'country': 'Portugal',
        'code': 'PPL',
        'id': 2017

    }, 'ERD': {
        'name': 'Eredivisie',
        'alt-name': 'Eredivisie',
        'country': 'Netherlands',
        'code': 'DED',
        'id': 2003

    }, 'FWC': {
        'name': 'FIFA World Cup',
        'alt-name': 'FIFA World Cup',
        'country': None,
        'code': 'WC',
        'id': 2000
    }
}


class Status(Enum):
    scheduled = 'SCHEDULED'
    live = 'LIVE'
    in_play = 'IN_PLAY'
    paused = 'PAUSED'
    finished = 'FINISHED'
    postponed = 'POSTPONED'
    suspended = 'SUSPENDED'
    cancelled = 'CANCELED'


class Plan(Enum):
    default = 'TIER_ONE'
    one = 'TIER_ONE'
    two = 'TIER_TWO'
    three = 'TIER_THREE'
    four = 'TIER_FOUR'


class Standing(Enum):
    default = 'TOTAL'
    home = 'HOME'
    away = 'AWAY'


# Not reading in any stages as of now
class Stage(Enum):
    default = 'REGULAR_SEASON'
    first_qual = '1ST_QUALIFYING_ROUND'
    second_qual = '2ND_QUALIFYING_ROUND'
    third_qual = '3RD_QUALIFYING_ROUND'
    playoff = 'PLAY_OFF_ROUND'
    group_stage = 'GROUP_STAGE'
    round_of_16 = 'ROUND_OF_16'
    quarter_finals = 'QUARTER_FINALS'
    semi_finals = 'SEMI_FINALS'
    finals = 'FINAL'