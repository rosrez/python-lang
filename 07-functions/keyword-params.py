#!/usr/bin/env python

# If the last argument of a function definition begins with **,
# all the additional keywordarguments (those that don't match
# any of the other parameter names

def make_table(name, **params):
    # Get configuration parameters from parms (a dict)
    fgcolor = parms.pop("fgcolor", "black")
    bgcolor = parms.pop("bgcolor", "white")
    width = parms.pop("width", None)

    print "fg = %s, bg = %s, width = %d" % (fgcolor, bgcolor, width)


# This invocation supplies many more parameters than our function processes. Also, 
# the caller need not know the exact order of parameters in the function definition

make_table([1,2,3,4], fgcolor="Blue", bgcolor="white", border=1, cellpadding=10, width=400)
