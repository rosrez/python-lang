#!/usr/bin/env python

# Demonstration of using generator expressions for declarative programming

lines = open("../txt/portfolio.txt")
fields = (line.split() for line in lines)                # generates a list of tuples out of lines
print(sum(float(f[1]) * float(f[2]) for f in fields))    # file I/O and split deferred until this statement

# The preceding version tends to run faster than the more traditional version below:

total = 0
for line in open("../txt/portfolio.txt"):
    fields = line.split()
    total += float(fields[1]) * float(fields[2])
print total
