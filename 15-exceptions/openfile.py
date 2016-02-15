#!/usr/bin/env python

import sys

def usage():
    print "Usage: %s filename" % sys.argv[0]
    quit(1)

if len(sys.argv) < 2:
    usage()

filename = sys.argv[1]

try:
    f = open(filename, "r")
    f.close()
    print "Successfully opened %s" % filename
except IOError as e:
    print e
