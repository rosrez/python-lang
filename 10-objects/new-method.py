#!/usr/bin/env python

# Demo of the __new__() method implementation.

# One reason for implementing custom __new__() methods in objects
# is when an object inherits from an immutable object (a number,
# a string or a tuple).
# __new__() is the only method that gets called prior to __init__(), where
# it is too late to modify the value of the object. This is where
# it is beneficial for a class to provide its own __new__() method.

class Upperstr(str):
    def __new__(cls, value=""):
        return str.__new__(cls, value.upper())

s = "hello"
u = Upperstr(s)

print s
print u
