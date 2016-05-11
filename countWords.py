'''
Use itemgetter to count appearances of words in an online text, sort in print the 3 most frequent ones
Created on May 5, 2016
@author: course
@author: dinh
'''

from operator import itemgetter
import urllib
handle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

counts = dict()
for line in handle:
    words = line.split() # split line into words
    for word in words:
        counts[word] = counts.get(word,0) + 1 # add new word to list or add 1 to old word
l = counts.items() # list of tuples (word, count)
l = sorted(l, key = itemgetter(1), reverse = True) # sort by counts in decreasing order
print l[:3]
