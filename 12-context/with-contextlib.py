#!/usr/bin/env python

from contextlib import contextmanager

# The contextlib module allows custom context managers to be
# more easily implemented by placing a wrapper around a generator function.
# Here is an example.

@contextmanager
def ListTransaction(thelist):
    print """\
'with' invokes the generator function 
that runs until the 'yield' statement"""
    workingcopy = list(thelist)
    yield workingcopy
    print """\
leaving 'with' context - the generator function 
resumes after 'yield'
"""
    # Modify the original list only if no errors
    thelist[:] = workingcopy

# In this example, the value passed to yield is used as the return value from __enter__().
# When the __exit__() method gets invoked, execution resumes after the yield. 

# If an exception gets raised in the context, it shows up as an exception in the
# generator function. If desired, an exception could be caught, but in this case,
# exception will simply propagate out of the generator to be handled elsewhere.

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
