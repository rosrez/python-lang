#!/usr/bin/env python

from random import randint

# Generate a list of random integers in [-10; 10] range
l = [randint(-10,10) for i in xrange(20)]
s = sorted(l)

print "Array of numbers: %s" % l
print "Sorted array: %s" % s
