#!/usr/bin/env python

from socket import *
s = socket(AF_INET, SOCK_STREAM)        # Create a TCP socket
s.connect(('localhost', 50000))         # Connect to the server: note the (host, port) tuple used!
tm = s.recv(1024)                       # Receive no more than 1024 bytes
s.close()
print "The time is %s" % tm.encode("ascii")
