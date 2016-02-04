#!/usr/bin/env python

# P2

principal = 1000;
rate = 0.05
numyears = 5
year = 1
f = open("file-output.out", "w")     # open file for writing
while year <= numyears:
    principal = principal * (1 + rate)
    # The >>f syntax works only in Python 2. 
    # In Python 3, we would use: print(what-to-print, file=f) 
    print >>f, "%3d %0.2f" % (year, principal)
    year += 1
f.close()
