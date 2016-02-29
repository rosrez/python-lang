#!/usr/bin/env python

# When nested functions are used, closures capture the entire environment
# needed for the inner function to execute.

# Closures and nested functions are especially useful if you want to write
# code based on the concept of lazy or delayed evaluation.

from urllib import urlopen
# from urllib.request import urlopen (Python 3)
def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page("http://www.python.org")

# Even though page() is no longer executing the get function object 
# (assigned to python variable) implicitly carries the values 
# of the outer variables that were defined when the get function was created.
# Thus, when get() executes, it calls urlopen(url) with the value of 'url'
# that was originally supplied to page().

pydata = python()       # This fetches http://www.python.org
print pydata

print "----------------------"
print "Printing python.closure:"
print python.__closure__
print python.__closure__[0]
