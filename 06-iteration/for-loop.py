#!/usr/bin/env python

print "Basic iteration"
for i in [1,2,3,4,5,6,7,8,9]:
    print "2 to the %d power is %d" % (n, 2**n)

# Note: in Python 2, range() creates a fully populated list,
# which is memory-consuming for large numbers of items. Use
# xrange() in Python 2 to yield items on demand. In Python 3,
# xrange() was renamed range().

print "Iteration using range"
for i in xrange(1,10):          # xrange() == range() in Python 3
    print "2 to the %d power is %d" % (n, 2**n) 
