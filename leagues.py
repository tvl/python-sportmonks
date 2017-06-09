#/usr/bin/python
from os import getenv
from sportmonks import *

token = getenv('SPORTMONKS_API_TOKEN')
init(token)

# Leagues
header = ['id', 'country_id', 'name', 'is_cup']
print(*header, sep=', ')
for l in get('leagues', paginated=False):
    row = [l['id'], l['country_id'], l['name'], bool(int(l['is_cup']))]
    print (*row, sep=', ')

