#!/usr/bin/env python

# ConfigParser class demo

try:
    from configparser import ConfigParser           # Python 3
except ImportError:
    from ConfigParser import ConfigParser           # Python 2

import os

# Dictionary of default variable settings
# Initially, this dictionary gets applied to all sections, 
# but can later be set individually on a per-section basis.
# We show the example of changing 'basedir' value in
# the 'input' section later in the script. The change 
# *does not* affect the value in the 'output' section.
defaults = {
    'basedir' : '~'             
}

filename = "configparser.ini"

# Create a ConfigParser object and read the .ini file
c = ConfigParser(defaults)
c.read(filename)

print "Config file keys are case-insensitive"
print "[output]: logfile = %s" % c.get('output','logfile')
print "[output]: LOGFILE = %s (the same key-value pair)" % c.get('output','logfile')
print "-" * 10,"\n"

print '''\
LOGGING is set to 'on' which is not legal Python syntax,
but works with Configparser'''
print "[output]: logging = %s ('on' in the .ini file) " % c.getboolean('output', 'logging')
print "-" * 10,"\n"

print "Generic operations - lists of items"
print "Sections: %s" % c.sections()
print "Options - [output]: %s" % c.options('output')
print "Options - [input]: %s" % c.options('input')
print "-" * 10,"\n"

# Update on one setting on a per-section basis

print "Generic operations - setting items"
c.set('input', 'basedir', os.environ['HOME'])
print "Set [input]: basedir = %s" % c.get('input', 'basedir'),
print "--> dependent options also change -- *only in this section*:"
print "[input]: indir = %s" % c.get('input', 'indir')
print "[input]: infile = %s" % c.get('input', 'infile')
print "Set [output]: basedir = %s" % c.get('output', 'basedir'),
print "--> remains the same!"

# After we write the changed config to file, we get
# an extra item basedir = /home/admin in the [input] section.

# Save the resulting configuration in a new file
outname = filename + ".out"
f = open(outname, "w")
c.write(f)              # write() requires that the file-like object be opened prior to the call
f.close()
