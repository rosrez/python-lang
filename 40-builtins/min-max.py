#!/usr/bin/env python

from random import randint

# Generate a list of random integers in [-10; 10] range
l = [randint(-10,10) for i in xrange(20)]
min = min(l)
max = max(l)

print "Array of numbers: %s" % l
print "Min value: %d, Max value: %d" % (min, max)
