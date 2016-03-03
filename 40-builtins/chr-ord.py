#!/usr/bin/env python

s = "Hello world"
a = bytearray(s)

print "chr(): restore character values from integer representation"
for i in a:
    print chr(i),
print

print "ord(): obtain ordinal values (character codes) from characters"
for c in s:
    print hex(ord(c)),
