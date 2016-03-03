#!/usr/bin/env python

import sys, subprocess

def usage():
    print "Usage: %s command" % sys.argv[0]
    sys.exit(1)

if len(sys.argv) < 2:
    usage()

cmdargs = sys.argv[1:]
argstr = " ".join(cmdargs)

print cmdargs
print "|%s|" % argstr

# From https://docs.python.org/2/library/subprocess.html

# The shell argument (which defaults to False) specifies whether to use 
# the shell as the program to execute. If shell is True, it is recommended 
# to pass args as a string rather than as a sequence.

p = subprocess.Popen(cmdargs, shell=False,
       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Ibidem:

# Popen.communicate(input=None)

# Note: The data read is buffered in memory, 
# so do not use this method if the data size is large or unlimited. 

out, err = p.communicate()

# In other words, p.communicate() can be used for relatively 
# simple one-time interactions between the script and the child process.

# We could try writing to p.stdin (p.stdin.write()) and reading from 
# p.stdout (p.stdout.read), but the same Python doc page says:

#  Warning: Use communicate() rather than .stdin.write, .stdout.read 
# or .stderr.read to avoid deadlocks due to any of the other OS pipe 
# buffers filling up and blocking the child process. 

print "type(out) = %s" % type(out)
print "type(err) = %s" % type(err)

print "Command output ----"
print out
print "Command error ----"
print err
