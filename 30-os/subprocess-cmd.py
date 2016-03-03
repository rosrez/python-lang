#!/usr/bin/env python

import sys, subprocess

def usage():
    print "Usage: %s filter command" % sys.argv[0]
    sys.exit(1)

if len(sys.argv) < 3:
    usage()

filter = sys.argv[1]
cmdargs = sys.argv[2:]

p = subprocess.Popen(cmdargs, shell=False,
       stdout=subprocess.PIPE)

out = p.stdout

for l in out:
    if filter in l:
        print l,



