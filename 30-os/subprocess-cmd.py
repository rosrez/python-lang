#!/usr/bin/env python

import sys, subprocess

def usage():
    print "Usage: %s command" % sys.argv[0]
    sys.exit(1)

if len(sys.argv) < 2:
    usage()

p = subprocess.Popen(sys.argv[1:], shell=True, # stdin=subprocess.PIPE,
       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()

print "Command output ----"
print out
print "Command error ----"
print err
