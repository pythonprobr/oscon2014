#!/usr/bin/env python3

from urllib import request

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
FILENAME = 'osconfeed.json'

print('saving %s to %s' % (URL, FILENAME))

with request.urlopen(URL) as remote, open(FILENAME, 'wb') as local:
    local.write(remote.read())
