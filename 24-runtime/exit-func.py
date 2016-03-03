#!/usr/bin/env python

# Demonstrates registration of exit handlers

import atexit, time
import gc               # garbage collector module

# Our custom exit handler

def cleanup():
    print "Exit function: cleaning up"

# Register exit handlers
# Garbage collector is not normally called when Python interpreter terminates the program

atexit.register(cleanup)
atexit.register(gc.collect)         # we can even register a garbage collector invocation

# Wait for something to happen (i.e user pressing Ctrl-C)

print "Starting a lengthy process (going to sleep for 30 secs)"
time.sleep(30)
