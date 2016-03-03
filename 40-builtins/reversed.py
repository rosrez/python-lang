#!/usr/bin/env python

from random import randint

# Generate a list of random integers in [-10; 10] range
l = [randint(-10,10) for i in xrange(20)]
r = reversed(l)

print "Array of numbers: %s" % l
print "Array in reverse order: %s" % l

# We can employ slicing to reverse items in a sequence,
# but this may be convenient for list comprehensions

s = [-i for i in reversed(l)]
print "Array in reverse order with reversed signs: %s" % s

# Although slicing works here as well. reversed() produces an
# iterator, so it might be faster to operate. Slicing will
# generate a sequence all at once

s = [-i for i in l[::-1]]
print "Array in reverse order with reversed signs: %s" % s


