#!/usr/bin/env python

# Abstract base classes demo.

from abc import ABCMeta, abstractmethod, abstractproperty

class Foo(object): 
    __metaclass__ = ABCMeta        # In Python 3, you use the syntax class Foo(metaclass=ABCMeta)

    @abstractmethod
    def doit(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass

class Bar(Foo):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Bar object: name = %s" % self.__name

    # redefining the abstract method
    def doit(self, a, b):
        print "My name is %s - I'm doing %d ~ %d" % (self.name, a, b)

    # redefining the abstract property: note that it's ok to define setters and
    # deleters, even if the abstract base class didn't define them.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

class Baz(Foo):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Baz object: name = %s" % self.__name

# Try to instantiate Foo -- fails with TypeError

try:
    f = Foo()
except TypeError as e:
    print "Foo: Abstract base classes cannot be instantiated!"
    print e
print "--------------\n"

# Try to instantiate Baz, which doesn't redefine Foo's abstract methods/properties -- fails with TypeError

try: 
    bz = Baz("BAZ")
except TypeError as e:
    print '''Baz: Descendants of abstract classes with undefined abstract methods
are also treated as abstract classes'''
    print e
print "--------------\n"

# Instantiate Bar, which does redefine abstract methods/properties -- succeeds

b = Bar("Alpha")
print b
b.name = "Omega"
print b
b.doit(5, 6)
print "--------------\n"
