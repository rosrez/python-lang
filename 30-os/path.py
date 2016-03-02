#!/usr/bin/env python

import sys, os.path

def pathfunc(func, path):
    print "%s(%s) = %s" % (func.__name__, path, str(func(path)))

path = sys.argv[0]                  # script name - always exists
fullpath = os.path.abspath(path)    # get full path - more suitable for some tests 

funcs = [
    os.path.abspath,
    os.path.basename,
    os.path.dirname,
    os.path.exists,
    os.path.getatime,
    os.path.getctime,
    os.path.getmtime,
    os.path.getsize,
    os.path.isfile,
    os.path.isdir,
    os.path.islink,
    os.path.ismount
]

# Call each function in the list, in turn

for f in funcs:
    if f == os.path.dirname or f == os.path.basename:
        pathfunc(f, fullpath)
    else:
        pathfunc(f, path)
