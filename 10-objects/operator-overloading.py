#!/usr/bin/python

class Complex(object):
    def __init__(self, real, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    # Returns a string that can be evaluated to recreate the object,
    # i.e. "Complex(real, imag)". This convention should be followed for all user-defined
    # objects as applicable.
    def __repr__(self):
        return "Complex(%s, %s)" % (self.real, self.imag)

    # This returns a 'nicely formatted' version of an object 
    # that is used by the print statement/function.
    def __str__(self):
        return "(%g+%gj)" % (self.real, self.imag)
    
    # self + other
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # self - other
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # other + self (note that the order of parameters is identical to that of __add__()
    def __radd__(self, other):
        return Complex(other.real + self.real, other.imag + self.imag)

    # other - self (note that the order of parameters is identical to that of __sub__()
    def __rsub__(self, other):
        return Complex(other.real - self.real, other.imag - self.imag)


# Create some Complex objects
c = Complex(5,1)
print "c = %s" % c
a = Complex(3,2)
s = Complex(4,1)
print "%s + %s = %s" % (c, a, c + a)
print "%s - %s = %s" % (c, s, c - s)

# The following also works, partly by accident, since all Python built-in types
# already have the .real and .imag attributes.

ra = 3
rs = 4

print "%s + %s = %s" % (c, ra, c + ra)
print "%s - %s = %s" % (c, rs, c - rs)

# However, the operation 4 + c dosn't work out of the box because the built-in floating
# point type doesn't know anythin about the Complex class. To fix this, we can
# add the reverse operand methods (radd, rsub).

print "%s + %s = %s" % (ra, c, ra + c)
print "%s - %s = %s" % (rs, c, rs - c)
