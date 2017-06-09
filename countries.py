#/usr/bin/python
from os import getenv
from sportmonks import *

token = getenv('SPORTMONKS_API_TOKEN')
init(token)

# Countries
header = ['id', 'world_region', 'continent', 'sub_region', 'name']
print(*header, sep=', ')
countries = get('countries', paginated=False)
for c in countries:
    extra = c['extra']
    if extra:
        row = [c['id'], extra['world_region'], extra['continent'], extra['sub_region'], c['name']]
    else:
        row = [c['id'], None, None, None, c['name']]
    print(*row, sep=', ')

