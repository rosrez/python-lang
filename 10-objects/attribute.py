#!/usr/bin/env python

# Whenever an attribute is set using obj.name = value,
# the special method obj.__setattr__("name", value) is invoked.
# If an attribute is deleted using del obj.name, the special method 
# obj.__delattr__("name") is invoked. The default behavior of these
# methods is to modify or remove values from the local __dict__
# of obj unless the requested attribute happens to correspond to a
# property or descriptor. In that case, the set and delete operation
# will be carried out by the set and delet functions associated
# witht the property.

class Foo(object):
    def __init__(self, name):
        self.name = name

# Upon creation, f will have one user-defined attribute, name,
# as specified in the constructor
f = Foo("Monty")
print "f.name is now %s" % f.name

# All these features are stored in Foo.__dict__ dictionary as key-value pairs
print "f.__dict__ now is:",f.__dict__
print "---------------"

# We can create any additional attributes on the fly, like this:
f.last_name = "Python"
print "f.last_name is now %s" % f.last_name
print "f.__dict__ now is:",f.__dict__
print "---------------"

f.feature = "turbo"
print "f.feature is now %s" % f.feature
print "f.__dict__ now is:", f.__dict__
print "---------------"

# It is possible to directly assign values to __dict__
f.__dict__["new_feature"] = "extra"
print "f.new_feature is %s" % f.new_feature
print "f.__dict__ now is:",f.__dict__
