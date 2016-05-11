'''
Use json to parse the content of geojson at entered location and retrive its place_id
Created on May 7, 2016
@author: course
@author: dinh
'''

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# looping through entered locations
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break # exit if no location entered

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address}) # format url
    print 'Retrieving from', url
    handle = urllib.urlopen(url)
    data = handle.read()
    print 'Retrieved',len(data),'characters'

    # load data into json format and check if it is ok, otherwise restart loop
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # print json.dumps(js, indent=2) # dump into view
    print type(js)

    place_id = js['results'][0]['place_id']
    print 'place_id', place_id