'''
Use socket to access a website and receive first 500 characters
Created on May 6, 2016
@author: course
@author: dinh
'''

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # standard protocol
mysock.connect(('www.pythonlearn.com', 80)) # through port 80
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n') # send GET request

while True:
    data = mysock.recv(500) # receive first 500 characters
    if (len(data) < 1):
        break
    print data

mysock.close()