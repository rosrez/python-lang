#!/usr/bin/env python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello World", ("", 50000))       # Note the (host, port) tuple used as destination
resp, addr = s.recvfrom(256)
print resp
s.sendto(b"Spam", ("", 50000))
resp, addr = s.recvfrom(256)
print resp
s.close()
