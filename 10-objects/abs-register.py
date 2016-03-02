#!/usr/bin/env python

# Demo of registering a class with an abstract base class.

from abc import ABCMeta, abstractmethod, abstractproperty

class Foo(object): 
    __metaclass__ = ABCMeta        # In Python 3, you use the syntax class Foo(metaclass=ABCMeta)

    @abstractmethod
    def doit(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass

# A new class unrelated to Foo.
# We define properties/methods from Foo: name and doit().

class Bar(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Bar object: name = %s" % self.__name

    # define Foo's interface method
    def doit(self, a, b):
        print "My name is %s - I'm doing %d ~ %d" % (self.name, a, b)

    # define Foo's interface property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

# Since we defined properties/methods from Foo: name and doit(),
# we can register the Bar class with abstract class Foo, so Foo becomes
# Bar's abstract class ancestor.

Foo.register(Bar)

# Instantiate Bar

b = Bar("Alpha")
print b
b.name = "Omega"
print b
b.doit(5, 6)

# Now the inheritance-based type checking works with Foo,
# so we are sure that our object implements the Foo's interface

print "isinstance(b, Foo) = %s" % isinstance(b, Foo)        # returns True
