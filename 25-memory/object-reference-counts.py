#!/usr/bin/env python

import sys

a = 37      # Creates an object with value 37
print "a = 37"
print "refcount of a = %d" % sys.getrefcount(a)

b = a       # Increases reference count of 37
print "b = a"
print "refcount of a = %d" % sys.getrefcount(a)

c = []
c.append(b) # Increases count on 37
print "c = []\nc.append(b)"
print "refcount of a = %d" % sys.getrefcount(a)

print "b = 42"
b = 42      # Decrease reference count of 37
print "refcount of a = %d" % sys.getrefcount(a)

print "c[0] = 2.0"
c[0] = 2.0  # Decrease reference count of 37
print "refcount of a = %d" % sys.getrefcount(a)

print "del a"
del a       # Decrease reference count of 37
print "refcount decreases but is no longer accessible via a"

