#!/usr/bin/env python

# Illustrates optional parameters

# This function defines one mandatory parameter (msg)
# and one optional (char). Optional parameters must follow
# all mandatory parameters in the function definition

def print_line(msg, char = '-'):
    print char * 10, msg, char * 10

print_line("Chapter 1")
print_line("Chapter 2", "+")

# Here, the default value x = a captures the value of a when the function is defined.
# Any subsequent redefinitions of 'a' don't have an impact on foo().

a = 10
def foo(x = a):
    return x

a = 5
print "Despite a is redefined to 5, the foo() function returns x = a = %d" % foo()

# The use of mutable objects as default values can lead to unintended behavior.
# Here, the default argument retains modifications made from previous invocations.

def bar(x, items=[]):
    items.append(x)
    return items

print bar(1)          # returns [1]
print bar(2)          # returns [1, 2]
print bar(3)          # returns [1, 2, 3]

# We can prevent this behavior by using the None value for the mutable value

def bar(x, items = None):
    if items is None:
        items = []
    items.append(x)
    return items

print bar(1)                            # returns [1]
print bar(2)                            # returns [2]
print bar(3)                            # returns [3]
print (bar(10), [1, 2, 3, 4, 5])    # returns [1, 2, 3, 4, 5, 10]

