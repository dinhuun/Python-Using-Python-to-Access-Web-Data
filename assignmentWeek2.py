'''
Use regular expressions to find all numbers in text and add up
Created on May 5, 2016
@author: course
@author: dinh
'''

import re # import regular expressions
handle = open('regex_sum_270979.txt')

allNumbers = list()
for line in handle:
    line = line.strip()
    numbers = re.findall('[0-9]+', line) # find all number strings in each line
    for number in numbers:
        allNumbers.append(int(number)) # convert to integer and store in allNumbers
print sum(allNumbers)