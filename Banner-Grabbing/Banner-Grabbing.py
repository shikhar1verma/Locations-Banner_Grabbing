#!/usr/bin/env python
'''
this is an another script for grabbing the
banner of a website by only  giving the name
as the input by the user.
'''

import socket               #importing the socket library
from socket import *

Host = str(raw_input("Input the URL of Website: "))             #user input of website name

try:
	t = gethostbyname(Host)                                 #changing the name to ip address
except:

        print "[-] Cannot resolve '%s': Unknown host"%Host
	exit(0)



conn = socket(AF_INET,SOCK_STREAM)
conn.connect((t,80))                                            #trying to make a connection with webserver

try:
	conn.send('GET HTTP/1.1 \r\n')                          #sending the understandable request to the webserver
	ret=conn.recv(1024)
	print '[+]'+str(ret)
except Exception,e:
	print '[-] Unable to grab any information:'+ str(e)

conn.close()                                                    #closing the connection
