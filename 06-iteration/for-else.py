#!/usr/bin/env python

import sys

filename = "/etc/passwd"

def usage(msg):
    print "%s" % msg
    raise SystemExit(1)

if len(sys.argv) < 2:
    usage("supply username")

user = sys.argv[1]

for l in open(filename):
    if l.find(user) != -1:
        break;
# The 'else' clause is executed if the loop runs to completion 
# (includes the case when it's not run at all).
# In other words, the else block runs only if break is not executed.
else:
    print "User %s not found in %s" % (user, filename)
    raise SystemExit(1)

print "User %s entry in %s:" % (user, filename)
print l,
