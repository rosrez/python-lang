#!/usr/bin/env python

import os, signal

def handler(signum, frame):
    print "Caught SIGALRM"

# install the signal handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# loop 3 times setting an alarm for 3 sec and pausing to wait for signals
for i in xrange(3):
    signal.alarm(3)
    signal.pause()          # wait for signals
print "Done."
