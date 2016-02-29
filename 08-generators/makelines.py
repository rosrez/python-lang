#!/usr/bin/env python

# Tail a file (like tail -f)
# Example of a generator function

import sys
import time

def usage():
    print "Usage: %s filename" % (sys.argv[0])
    quit(1)

if len(sys.argv) < 2:
    usage()

# Open file for writing
f = open(sys.argv[1], "w")
# Write 2000 lines to file
for line in range(1,2001):
    print >>f, "Line %d " % line         # >>f (Python 2 specific) outputs to file f
    time.sleep(1)
f.close()
