'''
Use json to parse the content of json url and retrive its place_id
Created on May 7, 2016
@author: course
@author: dinh
'''

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_270985.json'
url = serviceurl + urllib.urlencode({'sensor':'false'}) # format url

print 'Retrieving from', url
handle = urllib.urlopen(url)
data = handle.read()
print data
print 'Retrieved', len(data), 'characters'

js = json.loads(str(data)) # js is dictionary {('note':'This file...', ('comments': list of 50 dictionaries)}
print json.dumps(js, indent=2)
l = js['comments'] # list of 50 dictionaries
total = 0
for item in l:
    total = total + int(item['count']) # accumulate value of key 'count' in list l of 50 dictionaries
print 'Count:', len(l)
print 'Sum:', total