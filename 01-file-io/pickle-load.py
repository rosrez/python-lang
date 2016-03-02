#!/usr/bin/env python

# Demo of restoring objects from a file

import pickle
from employee import Employee

filename = "employee.out"

f = open(filename, 'rb')        # opens file for binary input
e1 = pickle.load(f)             # load object from f
e2 = pickle.load(f)             # load object from f
f.close()

print "Loading objects from %s" % filename
for e in (e1, e2):
    print e
