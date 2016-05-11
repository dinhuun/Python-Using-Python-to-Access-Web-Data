'''
Use BeatutifulSoup to fin all numbers of comments in 'span' tags and add up
Created on May 6, 2016
@author: course
@author: dinh
'''

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_270984.html'
page = urllib.urlopen(url).read()

soup = BeautifulSoup(page) # error that still runs, cleans up page into soup
tags = soup('span') # find all 'span' tags
total = 0
for tag in tags:
    total = total + int(tag.contents[0]) # or tag.name, tag.attrs, tag.contents
print 'Count', len(tags)
print 'Sum', total