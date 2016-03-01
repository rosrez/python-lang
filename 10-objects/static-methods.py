#!/usr/bin/env python

# Static method demo. 

import time

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "%02d/%02d/%4d" % (self.month, self.day, self.year)  # American-style date

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

# Example of creating some dates
a = Date(1967, 4, 9)
b = Date.now()          # Calls static method now()
c = Date.tomorrow()     # Calls static method tomorrow()

for d in (a, b, c):
    print d
