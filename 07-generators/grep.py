#!/usr/bin/env python

# This script mimics basic grep (operates on a single file)
# Example of a generator function.

import sys

def usage():
    print "Usage: %s what filename"
    quit(1);

# The function returns only lines of text that contain given string
def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

if len(sys.argv) < 3:
    usage()

what = sys.argv[1]
file = sys.argv[2]

f = open(file)
for line in grep(f.readlines(), what):
    print line,
f.close()
