#!/usr/bin/python3

import sys

# sys.stdout is a file object, we're invoking its write() method
sys.stdout.write("Enter your name: ")
# sys.stdin is a file object, we're invoking its readline() method
name = sys.stdin.readline()
 # note the trailing comma - readline preserves the trailing newline
print "Hello", name,  

# In Python 2, the above is equivalent to:
# name = raw_input("Enter your name: ")

# In Python 3, the above is equivalent to:
# name = input("Enter your name: ")
