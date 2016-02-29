#!/usr/bin/env python

enable_tracing = True

def trace(func):
    # tracing enabled: surround the call to supplied function with debug output
    if enable_tracing:
        def callf(*args, **kwargs):
            print "Calling %s: %s, %s" % (func.__name__, args, kwargs)
            r = func(*args, **kwargs)
            print "%s returned %s" % ( func.__name__, r)
            return r
        # This will return the inner function object to the caller
        return callf
    # tracing disabled: call the supplied function unmodified
    else:
        return func

@trace
def square(x):
    return x*x


square(5)
square(7)
square(9)
