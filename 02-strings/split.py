#!/bin/python3

import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " delimiter [filename]")
    exit(1)

delim = sys.argv[1]         # delimiter

if len(sys.argv) == 2:
    fh = sys.stdin          # assume stdin if user provided no filename
else:
    fh = sys.argv[2]        # filename, if provided

n = 1
for line in fh.readlines():
    entry = line.strip().split(delim)
    for i in range(1,len(entry)):
        print("%4d: $%s = [%s]" % (n, i, entry[i]))
    n = n + 1

fh.close()
