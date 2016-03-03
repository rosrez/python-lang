#!/usr/bin/env python

import sys

print "sys.path: %s" % sys.path
print "sys.platform: %s" % sys.platform

print "bite order: %s" % sys.byteorder

print "Python executable: %s" % sys.executable
print "Python version: %s" % sys.version
print "Python version (tuple): %s" % list(sys.version_info)
