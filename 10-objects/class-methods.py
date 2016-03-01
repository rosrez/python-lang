#!/usr/bin/env python

# Class method demo. 

import time

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "%02d/%02d/%4d" % (self.month, self.day, self.year)  # American-style date

    @classmethod
    def now(cls):                                   # accepts a class object
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # cls() constructs an object of class 'cls'

    @classmethod
    def tomorrow(cls):                              # accepts a class object
        t = time.localtime(time.time() + 86400)
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # cls() constructs an object of class 'cls'

# This class is derived from Date. Its __str__ method is rewritten to 
# output European style dates (day-of-month first).
# However, if we had declared our 'factory' methods as static,
# they would have returned objects of Date class.
# Class methods are a way around this constraint: they produce instances
# of the class they are invoked from.

class EuroDate(Date):
    # Modify string conversion to use European dates
    def __str__(self):
        return "%02d/%02d/%04d" % (self.day, self.month, self.year) # European style date

# Note that here, we don't supply the class object explicitly. Instead Python sets the cls
# argument to now() to either Date or Eurodate, depending on what class we're calling the
# class method on.

a = Date.now()          # Calls Date.now(Date) and returns a Date
e = EuroDate.now()      # Calls Date.now(Eurodate) and returns a Eurodate

print "Now is %s (American style) or %s (European style)" % (a, e)
