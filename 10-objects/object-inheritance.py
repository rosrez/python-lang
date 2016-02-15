#!/usr/bin/env python

# Inherits from list class

class Stack(list):
    # Add push() method for stack interface
    # Note: lists already provide a pop() method
    def push(self, object):
        self.append(object)

s = Stack()         # Create a stack
s.push("Dave")      # Push some things onto it
s.push(42)
s.push([3,4,5])
x = s.pop()                 # x gets [3,4,5]
print "Popped %s" % str(x)
x = s.pop()                 # x gets 42
print "Popped %s" % str(x)
del s               # Destroy x
