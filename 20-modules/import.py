#!/usr/bin/env python

# Module import demo

# Basic module import demo

import module1, module2         # comma separated list of modules (we can also use multiple import statements)

s = "a quick brown fox jumped over a lazy dog"

# Now we can use functions from imported modules.
# We must refer to modules' individual namespaces
# followed by the dot (.) operator and the function name

print s
print module1.reverse(s)
print module1.split(s)
print module2.bracket(s)
print module2.titlecase(s)
