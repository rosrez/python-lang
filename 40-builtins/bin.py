#!/usr/bin/env python

# bin(x)
# Returns a string containing the binary representation of the integer x.
# Note that arguments are limited to integer values only.

# The function returns only the significant bits. 
# For example, it returns just 0b1 for b.
# It returns less than 32 bits for i4.

b = True
i4 = 0x012345678
i8 = 0xfedcba9876543210

for v in (b, i4, i8):
    print "bin(%s) = %s" % (v, bin(v))
