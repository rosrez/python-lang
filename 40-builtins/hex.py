#!/usr/bin/env python

# hex(val)
# Generates a string with hexadecimal representation of val.

# The program produces the following output:

# $ python hex.py
# 0x48 0x65 0x6c 0x6c 0x6f 0x20 0x77 0x6f 0x72 0x6c 0x64

a = bytearray("Hello world")
for b in a:
    print hex(b),
