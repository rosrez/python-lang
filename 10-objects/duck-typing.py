#!/usr/bin/env python

# Demo of 'duck typing', a feature of Python that allows
# objects implementing the same interface (fields, names)
# to be treated in the same manner, even if they are not related.

# Here, we have two classes that share a number of fields:
# 'name' and 'address'. We can iterate over a heterogenous list
# of items that have the same interface and use the same
# members from different items seamlessly.

class Employee(object):
    def __init__(self, name, address, grade):
        self.name = name
        self.address = address
        self.grade = grade

class Customer(object):
    def __init__(self, name, address, code):
        self.name = name
        self.address = address
        self.code = code

# Create Employee instance
e = Employee("John", "Baker Str. 17", 7)

#
c = Customer("MacroSoft", "Technology Ave 4", 12345)

for item in (e, c):
    print "%s -- %s" % (item.name, item.address)
