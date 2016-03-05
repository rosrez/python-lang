#!/usr/bin/env python

# The key aspect of the SocketServer/socketserver module is that 
# handlers are decoupled from servers. That is, once you
# have written a handler, you can plug it into many different kinds
# of servers without having to change its implementation.

try:
    from socketserver import BaseRequestHandler   # Python 3
    from socketserver import TCPServer
    from socketserver import UDPServer
except ImportError:
    from SocketServer import BaseRequestHandler # Python 2
    from SocketServer import TCPServer
    from SocketServer import UDPServer

import socket
import time
import sys

# Handler class that implements a simple time server 
# that operates with streams or datagrams

class TimeHandler(BaseRequestHandler):
    def handle(self):
        resp = time.ctime() + "\r\n"
        if isinstance(self.request, socket.socket):
            # A stream-oriented connection
            self.request.sendall(resp.encode("latin-1"))
        else:
            # A datagram-oriented connection
            self.server.socket.sendto(resp.encode("latin-1", self.client_address))

# To use a handler, it has to be plugged into a server object.
# There are four basic server classes defined:
#
# TCPServer, UDPServer, UnixStreamServer, UnixDatagramServer

port = 50000

# If no command argument is provided, assume TCP server mode
mode = "tcp"
if len(sys.argv) > 1:
    if sys.argv[1] != "tcp" and sys.argv[2] != "udp":
        print "Usage: %s [tcp|udp]" % (sys.argv[1])
        sys.exit(1)
    
if mode == "tcp":
    serv = TCPServer(("", port), TimeHandler)
else:
    serv = UDPServer(("", port), TimeHandler)

serv.serve_forever()
