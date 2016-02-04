#!/usr/bin/env python3

import sys

# 1. sys.argv is used to access command line arguments.
# 2. sys.argv is a list. This means that it is zero-based. It's length can be checked with len(sys.argv).
# 3. sys.argv always has at least one element, which is the scripts name (i.e., sys.argv[0] == <script_name>).

if len(sys.argv) == 1:
    fh = sys.stdin
else:
    fh = open(sys.argv[1])

for line in fh.readlines():
    # The trailing comma tells Python not to append newline to the output 
    # (the line just read has a newline already)
    print line,
    # print(line, end='')     # Python 3
fh.close()
