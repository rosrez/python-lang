#!/usr/bin/env python

l = [1, 2, 3] 
d = { 1: "one", 2: "two", 3: "three"}

print "list: %s -- %s" % (l, type(l))
print "dict: %s -- %s" % (d, type(d))
print

for i in (l, d):
    if type(i) is list:
        i.append(4)
    elif type(i) is dict:
        i[4] = 'four'

    print i
