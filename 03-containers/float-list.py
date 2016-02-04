#!/usr/bin/python2

import sys
if len(sys.argv) != 2:
    print "Please supply a filename"
    raise SystemExit(1)

f = open(sys.argv[1])           # Filename on command line
lines = f.readlines()           # Read all lines into a list
f.close()

# Convert all of the input values from strings to floats
# This is called LIST COMPREHENSION
fvalues = [float(line) for line in lines]
# We could even write the same line like this
# fvalues = [float(line) for line in open(sys.argv[1]]

# Print min and max values
print "The minimum value is ", min(fvalues)
print "The maximum value is ", max(fvalues)
