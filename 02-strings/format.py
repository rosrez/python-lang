#!/usr/bin/env python

i = 52
f = 115.5777

# Here, {0} and {1} refer to positional arguments to format.
# {1:format} is used for format specifier for argument 1

print "012345678901234567890 (", i, f, ")"
print "{0:5d} {1:0.2f}".format(i, f)

