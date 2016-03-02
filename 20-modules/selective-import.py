#!/usr/bin/env python

from module1 import split,reverse       # puts module1.split, module1.reverse into the current namespace
from module2 import titlecase           # puts module2.titlecase into the current namespace

s = "a quick brown fox jumped over a lazy dog"

print s
print reverse(s)            # module1. before reverse() would now be an error!
print split(s)              # no module1.split() anymore
print titlecase(s)          # no module2.titlecase() anymore
