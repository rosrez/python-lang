#!/usr/bin

# Using closures to preserve state across a series of function calls.
# Closures run much faster than corresponding OOP code.

import sys

def usage():
    sys.stderr.write("Usage closure2.py counter-start \n")
    raise SystemExit(1)

if len(sys.argv) < 2:
    usage()

counter_start = int(sys.argv[1])

def countdown(n):
    vars = { "n" : n }
    # next() preserves the state of n across invocations
    def next():
        r = vars["n"]
        vars["n"] -= 1
        return r
    return next

# Python 3 has a special nonlocal declaration 
# to reference variables that are neither local, nor global

def countdown3(n):
    # next() preserves the state of n across invocations
    def next():
        # nonlocal n --- commented out to prevent syntax error
        r = n 
        n -= 1
        return r
    return next

# Example use - function/closure
next = countdown(counter_start)
while True:
    v = next()
    if not v:   # reached zero
        break
    print v,
print

# The same functionality can be delivered by an object
class Countdown(object):
    def __init__(self, n):
        self.n = n
    def next(self):
        r = self.n
        self.n -= 1
        return r

# Example use -- object
c = Countdown(counter_start)
while True:
    v = c.next()
    if not v:   # reached zero
        break
    print v,
print
