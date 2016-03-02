#!/usr/bin/env python

# See import.py for explanation

def reverse(str):
    return str[::-1]

def split(str):
    return "-".join(str)

def unit_test():
    s = "ABCDEF"
    print s
    print reverse(s)
    print split(s)

# Check if running as a program

if __name__ == "__main__":
    # Yes, I'm running as main
    unit_test()
else:
    # I'm imported as a module - this may contain a setup section
    # that the module's symbols rely upon.
    pass
