#!/usr/bin/env python

import sys


# A generator function that can be combined with I/O functions

def countdown(n):
    while n > 0:
        yield "Next value: %d\n" % n
        n -= 1
    yield "End of output\n"

# Using a generator allows us to process generator output
# in different ways: output to file, socket, string.

f = sys.stdout          # f could be any file

print "redirecting to stdout"
count = countdown(5)
f.writelines(count)     # redirect generator function output to file
print "----------"

print "combining in a single string"
count = countdown(7)
out = "".join(count)
print out,
