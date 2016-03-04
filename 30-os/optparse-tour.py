#!/usr/bin/env python

import optparse

p = optparse.OptionParser()

# A simple option, with no arguments
p.add_option("-t", action="store_true", dest="tracing")

# An option that accepts a string argument
p.add_option("-o", "--outfile", action="store", type="string", dest="outfile")

# An option requires an integer argument
p.add_option("-d", "--debuglevel", action="store", type="int", dest="debug")

# An option with a few choices
p.add_option("--speed", action="store", type="choice", dest="speeed",
        choices=["slow", "fast", "ludicrous"])

# An option taking multiple arguments
p.add_option("--coord", action="store", type="int", dest="coord", nargs=2)

# A set of options that control a common destination
p.add_option("--novice", action="store_const", const="novice", dest="mode")
p.add_option("--guru", action="store_const", const="guru", dest="mode")

# Set default values for the various option destinations
p.set_defaults(tracing=False,
                    debug=0,
                    speed="fast",
                    coord=(0,0),
                    mode="novice")

# Parse the arguments
opt, args = p.parse_args()

# Print option values
print "tracing  :", opt.tracing
print "outfile  :", opt.outfile
print "debug    :", opt.debug
print "speed    :", opt.speed
print "coord    :", opt.coord
print "mode     :", opt.mode

# Print remaining arguments
print "args     :", args
