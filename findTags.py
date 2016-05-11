'''
Use BeautifulSoup to find all 'a' tags in a webpage and get their 'href' addresses
Created on May 5, 2016
@author: course
@author: dinh
'''

import urllib
from BeautifulSoup import *

url = raw_input('Enter url:')
page = urllib.urlopen(url).read()
soup = BeautifulSoup(page) # error still runs
tags = soup('a') # find all 'a' tags
for tag in tags:
    print tag.get('href', None) # get 'href' address