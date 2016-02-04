#!/usr/bin/env python

(a, b, c, d, e) = "abcde";

# A long line of code can be split using a backslash at the end of the line:
# We need not care about indentation on the following line (it's concatenated to
# the previous line(s) internally by the interpreter.

if a == 'a' and b == 'b' and c == 'c' \
        and not d == 'x' and e == 'e':
    print "OK"
