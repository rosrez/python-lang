#!/usr/bin/env python

# Tail a file (like tail -f)
# Example of a generator function

# You could use the makelines.py script in this directory
# to create a sample file

import sys
import time

def usage():
    print "Usage: %s filename" % (sys.argv[0])
    quit(1)

def tail(f):
    f.seek(0, 2)    # Move to EOF
    while True:
        line = f.readline()     # Try reading a new line of text
        if not line:            # If nothing, sleep briefly and try again
            time.sleep(0.1)
            continue
        yield line

if len(sys.argv) < 2:
    usage()

f = open(sys.argv[1])
for line in tail(f):
    print line,
f.close()
