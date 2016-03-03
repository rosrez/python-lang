#!/usr/bin/env python

# Demonstrates the use of all() and any() builtin functions.

# all(s)
# Returns True if all of the values in the iterable s evaluate to True.

# any(s)
# Returns True if any of the values in the iterable s evaluate as True.

# Note that s can contain any objects.

# A wrapper to (1-argument) function that displays function calls in the form:
# func(arg) = res
def callf(func, arg):
    res = func(arg)
    print "%s(%s) = %s" % (func.__name__, arg, res)

all_ones = [1, 1, 1, 1, 1, 1, 1, 1]
one_one  = [0, 0, 0, 0, 1, 0]
all_zeroes = [0, 0, 0, 0]

# A list of miscelaneous objects, which includes a list, a bool and an int.
# False and 0 evaluate to boolean zero, but a non-empty list evaluates to True,
# even if its contents are all zeroes. So any() will return true for 
# misc_objs since one of its items evaluates to True.

l = [0, 0, 0]
misc_objs = [l, False, 0]   # non-empty list, bool, int

for arg in (all_ones, one_one, all_zeroes, misc_objs):
    for f in (all, any):
        callf(f, arg)
