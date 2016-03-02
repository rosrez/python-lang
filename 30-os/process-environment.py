#!/usr/bin/env python

import os

print "USER = %s" % os.environ["USER"]
print "HOME = %s" % os.environ["HOME"]

print "CWD: %s" % os.getcwd()
print "PID: %d" % os.getpid()
print "Parent PID: %d" % os.getppid()
print "GID: %d" % os.getgid()
print "Groups for this user: %s" % os.getgroups()

print "Login name: %s" % os.getlogin()
print "EUID: %d" % os.geteuid()
print "SID: %d" % os.getsid(os.getpid())

mask = os.umask(0777)
os.umask(mask)
print "umask: %s" % mask
print "uname: %s" % list(os.uname())

