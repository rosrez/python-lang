#!/usr/bin/env python

# Illustrates the use of functions as objects

# This function accepts a function object as a parameter,
# calls the function defined by the object and returns the function result.

# We also define a variable to 

x = 42
def callf(func):
    return func()

def helloworld():
    return "Hello world"

# Even if we supply printx() as an object to a function/context where
# x has a different value (as in case of callf() above), we still get
# the value of 37. Packaging of statements of a function together with
# the environment in which they execute is called a *closure*.

x = 37
def printx():
    print "x is now %d" % x

print "Return from callf: %s" % callf(helloworld)

callf(printx)
