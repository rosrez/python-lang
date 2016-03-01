#!/usr/bin/env python

# Functions in Python may return multiple values as tuples

import sys

def usage():
    sys.stderr.write("Usage: tuple-results.py divisor dividend\n")
    raise SystemExit(1)

def div(a,b):
    q = a / b
    r = a - b*q
    return (q,r)

if len(sys.argv) < 3:
    usage()

a = int(sys.argv[1])
b = int(sys.argv[2])

# div() returns a tuple, so assign the result 
# to the (q, r) tuple; () are optional here
q, r = div(a, b)

print "quotient = %d, remainder = %d" % (q, r)
