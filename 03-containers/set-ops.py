#!/usr/bin/env python

s = set([1, 3, 5, 7, 9])
print "Initial state of s:", s

s.add(11)       # Add a single item
print "add(): added 11:", s

s.update([13, 15, 17, 19])       # Add multiple items: notice that update() expects ONE iterable argument!
print "update(): added 13, 15, 17, 19:", s

s.remove(5)       # Add a single item
print "remove(): removed 5:", s
