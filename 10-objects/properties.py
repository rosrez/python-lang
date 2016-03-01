#!/usr/bin/env python

# Properties demo.

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    # Calculated readonly properties

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi * self.radius

c = Circle(4)
print "Circle of radius %.2f: area = %.2f, perimeter = %.2f" % \
        (c.radius, c.area, c.perimeter)
