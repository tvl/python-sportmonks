#!/usr/bin/python
import requests
import requests_cache
import json

api_token = ''
api_url = 'https://soccer.sportmonks.com/api/v2.0/'

def init(token):
    global api_token
    api_token = token

def get(endpoint, include=''):
    if include == '':
        payload = {'api_token': api_token }
    else:
        payload = {'api_token': api_token, 'include': include}
    r = requests.get(api_url + endpoint, params=payload)
    data = json.loads(r.text)
    return data

def matches(from_date, to_date = None, include = ''):
    """Get matches list"""
    if to_date is None:
        to_date = from_date
    return get('matches/{}/{}'.format(from_date, to_date), include)['data']

def continents():
    return get('continents')['data']

def countries():
    return get('countries')['data']

def leagues():
    return get('leagues')['data']

def seasons():
    return get('seasons')['data']

def fixtures():
    return get('fixtures/between/2017-05-01/2017-05-31')['data']

def venue(id):
    return get('venues/{}'.format(id))['data']

def teams(season):
    return get('teams/season/{}'.format(season))['data']

# Use cache
requests_cache.install_cache('sportmonks_cache', backend='sqlite', expire_after=24*3600)
