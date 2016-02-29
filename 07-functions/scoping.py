#!/usr/bin/env python

# This script illustrates scoping rules for functions

a = 42
def foo():
    a = 13
    print "inside foo(): a = %d" % a

foo()       # a is still 42
print "main program - after foo(): a = %d" % a

b = 37
def bar():
    global a            # 'a' is in global namespace
    a = 13              # 'global' for 'a' will make the changes visible globally
    b = 0               # but changes to b will not be visible
    print "inside bar(): a = %d, b = %d" % (a, b)

bar()       # a is now 13, b is still 37
print "main program - after bar(): a = %d, b = %d" % (a, b)

