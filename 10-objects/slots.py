#!/usr/bin/env python

# Demo of using __slots__ 

# When __slots__ is defined, the attribute names that can be 
# assigned on instances of the object are restricted to the
# names specified. Otherwise, an AttributeError exception is raised.

# __slots__ is designed as a performance optimization. An array-like
# structure gets created instead of __dict__, which provides better
# performance at the cost of being non-modifiable. If a script
# creates a lot of objects, using __slots__ can provide significant
# performance gains.

class Foo(object):
    __slots__ = ('name', 'code')    # restricts attributes to 'name' and 'code'

f = Foo()

f.name = "Bob"
f.code = 1234

try:
    f.extra = "extra feature"       # 'extra' isn't contained in __slots__, raises in AttributeError
except AttributeError as e:
    print e

print "f.name = %s, f.code = %d" % (f.name, f.code)

# Note that classes with __slots__ defined don't have a __dict__ dictionary,
# since slots completely replaces the storage for object attributes.

try:
    print f.__dict__
except AttributeError as e:
    print "Classes with __slots__ defined don't have a __dict__ attribute"
    print e

