#!/usr/bin/env python

# Note that the set() constructor expects a single argument. Implicit tuples don't work here
# so we cannot say: sn = set(1, 2, 3). This would result in a syntax error.

# Create a set out of a list
sn = set([1, 42, 73])
# Create a set out of a string
ss = set("Hello")

print "Set of numbers:", sn
print "Set of characters in a string:", ss
