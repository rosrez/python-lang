#!/usr/bin/env python

# Variable params and keyword arguments

import sys

# Asterisk at the last parameter in function definition 
# indicates a variable number of parameters

def fprintf(file, fmt, *args):  # The remaining arguments are placed in args as a tuple
    file.write(fmt % args)

def printf(fmt, *args):
    # Call another function and pass along args, as a tuple
    fprintf(sys.stdout, fmt, *args)

fprintf(sys.stdout, "calling fprintf() on %d, %f, %s\n", 42, 3.14, "test")
fprintf(sys.stdout, "calling printf() on %d, %f, %s\n", 42, 3.14, "test")
