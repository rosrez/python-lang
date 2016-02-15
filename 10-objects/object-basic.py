#!/usr/bin/env python

class Stack(object):
    # Note that the internal 'self' variable must be 
    # mentioned explicitly in method declarations
    # self can contain any number of fields

    def __init__(self):         # Constructor
        self.stack = [ ]        # Initialize the internal stack field to an empty list

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

s = Stack()         # Create a stack
s.push("Dave")      # Push some things onto it
s.push(42)
s.push([3,4,5])
x = s.pop()                 # x gets [3,4,5]
print "Popped %s" % str(x)
x = s.pop()                 # x gets 42
print "Popped %s" % str(x)
del s               # Destroy x
