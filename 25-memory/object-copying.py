#!/usr/bin/env python

# This script illustrates the behavior of references to mutable objects.

import copy

# Plain reference -----------

a = [1, 2, 3, 4]
b = a                   # b is a reference to a
if b is a:
    print "b is a"      # this gets printed
else:
    print "b is not a"

b[2] = -100             # modify an index through a reference
print a                 # the change is visible through 'a'
print

# Shallow copy --------------

a = [ 1, 2, [3,4] ]         # Note a[2] is itself a list
b = list(a)                 # Create a shallow copy of 'a'
if b is a:
    print "b is a"
else:
    print "b is not a"      # this gets printed

b.append(100)                           # modify b
print "b = %s -- modified" % b          # see that 'b' is modified
print "a = %s" % a                      # and 'a' is not

b[2][0] = -100                          # modify a mutable element inside b
print "b = %s -- mutable element modified" % b          # see that mutable element is modified
print "a = %s -- mutable element modified" % a          # mutable element also modified
print

# Deep copy -----------------

a = [ 1, 2, [3,4] ]         # Note a[2] is itself a list
b = copy.deepcopy(a)        # Create a shallow copy of 'a'
if b is a:
    print "b is a"
else:
    print "b is not a"      # this gets printed

b[2][0] = -100                          # modify a mutable element inside b
print "b = %s -- mutable element modified" % b          # see that mutable element is modified
print "a = %s" % a                                      # mutable element here is not modified

