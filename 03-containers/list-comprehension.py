#!/usr/bin/env python


# This creates a list of squares based on a list of numbers

nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)

# This does the same thing using list comprehension

squares2 = [n * n for n in nums]

for n in squares:
    print n,
print
for n in squares2:
    print n,
print

# You can use multiple for loops with (optional) conditional statements

a = [-3, 5, 2, -10, 7, 8]
b = "abc"

# This filters out negative numbers from a list
nonneg = [s for s in a if s >= 0]           # produces [5, 2, 7, 8]
print nonneg

tuples = [(x,y) for x in a
                for y in b
                if x > 0]                   # produces all combinations of nonnegative x and letters: a, b, or c
print tuples
print "x is visible after comprehension (Python 2) and retains its last value: x = %d" % x
print "y is visible after comprehension (Python 2) and retains its last value: y = %s" % y
