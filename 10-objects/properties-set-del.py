#!/usr/bin/env python

# Demo of writable property (with setter and deleter defined)

# Note that the underlying value is stored in __name. There is no naming
# convention for backing fields of properties, but the backing field
# *must* have a different name.

class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property                   # getter method
    def name(self):
        return self.__name

    @name.setter                # setter method
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter               # deleter method
    def name(self):
        raise TypeError("Can't delete name")


f = Foo("Guido")
print "f.name = %s" % f.name
f.name = "Monty"
print "f.name = %s" % f.name

try: 
    del f.name
except TypeError as e:
    print e
