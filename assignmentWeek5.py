'''
Use XML to find the contents of all 'count' nodes in tree and add up
Created on May 7, 2016
@author: course
@author: dinh
'''

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_270981.xml'
url = serviceurl + urllib.urlencode({'sensor':'false'})

print 'Retrieving from', url
handle = urllib.urlopen(url)
data = handle.read()
print data
print 'Retrieved', len(data), 'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count') # get to count nodes more quickly than going through tree
total = 0 
for count in counts:
    total = total + int(count.text) # convert text in each 'count' node to integer and accumulate
print 'Count:', len(counts)
print 'Sum:', total
