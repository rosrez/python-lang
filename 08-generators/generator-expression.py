#!/usr/bin/env python

# Generator objects demo.

# Note that generator expressions do not produce a sequence,
# so their result cannot be indexed, appended to, etc.
# However, generator expressions can be converted into
# a list with the built-in list() function

import sys

# Read a file
f = open(sys.argv[0])                           # Open a file

# The two generator expressions below don't actually
# read the entire file into memory

lines = (t.strip for t in f)                    # Read lines, strip trailing/leading whitespace
comments = (t for t in lines if t[0] == "#")    # All comments

# The lines of the file are actually read when the
# program starts iterating in the 'for' loop. 
# During this iteration, the lines of the file are produced 
# upon demand and filtered accordingly.

for c in comments:
    print c
