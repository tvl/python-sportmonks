# python-sportmonks
Wrapper over the data provided SportMonks Soccer API

## Installation

Install it yourself as:

    $ git clone git@github.com:tvl/python-sportmonks.git

## Usage

The package has methods for gets some data from SportMonks.

```python
#/usr/bin/python
from sportmonks import *

token = '__YOURTOKEN__'
init(token)

# Continents
print('Continents:')
for a in continents():
    print(a['id'], a['name'])

# Countries
print('Countries:')
for c in countries():
    print(c['id'], c['name'])

# Leagues
print('Leagues:')
for l in leagues():
        print(l['id'], l['name'])

# Seasons
print('Seasons:')
for s in seasons():
        print(s['id'], s['attributes']['name'])

# Fixtures
print('Fixtures:')
for f in fixtures():
        print(f['id'], f['league_id'], f['season_id'])

```
If your have FREE PLAN your see:
```bash
Continents:
1 Europe
Countries:
320 Denmark
1161 Scotland
Leagues:
271 Superliga
501 Premiership
Seasons:
1273 2005/2006
1274 2006/2007
1275 2007/2008
1276 2008/2009
1277 2009/2010
1278 2010/2011
1279 2011/2012
1280 2012/2013
1281 2013/2014
1282 2014/2015
1286 2015/2016
759 2016/2017
1927 2005/2006
1928 2006/2007
1929 2007/2008
1930 2008/2009
1931 2009/2010
1932 2010/2011
1933 2011/2012
1934 2012/2013
1935 2013/2014
1936 2014/2015
1937 2015/2016
825 2016/2017

```
