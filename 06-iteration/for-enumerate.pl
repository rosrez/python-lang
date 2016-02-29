#!/usr/bin/env python

list = [2, 4, 6, 8, 10];

print "Iteration using enumerate to get index"
for i,n in enumerate(list):                 # enumerate(s), where s is a sequence, returns a tuple (index, item)
    print "squares[%d] = %d**2 = %d" % (i, n, 2**n) 
