'''
Use BeautifulSoup to follow the 18th hyperlink in each page for 7 times
Created on May 6, 2016
@author: course
@author: dinh
'''

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Bayleigh.html' # starting page
n = 7
while n > 0:
    page = urllib.urlopen(url).read() # read page of url
    soup = BeautifulSoup(page) # clean up
    tags = soup('a') # find all 'a' tags
    url = tags[17].get('href', None) # get the 18th hyperlink and repeat
    print url
    n = n-1