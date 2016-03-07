#!/usr/bin/env python

# The ListTransaction class below implements the context management
# protocol (i.e. the __enter__() and __exit__() methods.)

class ListTransaction(object):
    def __init__(self, thelist):
        self.thelist = thelist
    def __enter__(self):
        print "'with' statement implicitly calls __enter__() -- entering context"
        self.workingcopy = list(self.thelist)
        return self.workingcopy
    def __exit__(self, exctype, value, tb):
        print "exiting 'with' block implicitly callse __exit__()__ -- exiting context"
        if exctype is None:
            self.thelist[:] = self.workingcopy
        return False

# The preceding class allows one to make a sequence
# of modifications to an existing list. However,
# the modifications only take effect if no exceptions occur.
# Otherwise, the original list is lef unmodified.

items = [1, 2, 3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
print items         # Produces [1,2,3,4,5]

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("We're hosed!")
except RuntimeError:
    pass
print items
