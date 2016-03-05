#!/usr/bin/env python

from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)        # Create a TCP socket
s.bind(('', 50000))                     # Bind to port 50000: note the (host, port) tuple used!
s.listen(5)                             # 5 pending connections

while True:
    client, addr = s.accept()           # Get a connection
    print "Got a connection from %s" % str(addr)
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode("ascii"))
    client.close()
