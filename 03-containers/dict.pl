#!/usr/bin/env python

import sys;

def usage(dict):
    print "Available stock quotes"
    for key in dict:
        print key,
    print       # terminating newline
    quit(1)

prices = {
    "GOOG" : 490.10,
    "AAPL" : 123.50,
    "IBM"  : 91.50,
    "MSFT" : 52.13
}

if len(sys.argv) < 2:
    usage(prices)

qkey = sys.argv[1]

# Note that 'in prices' refers to the list of KEYS!
if qkey in prices:
    print "Quote for <%s> is %.2f" % (qkey, prices[qkey])
else:
    print "Found no quote for <%s>" % qkey

# Also note that we could get the value like this:
# val = prices.get(qkey, None)
#       KEY  -------^     ^-------- DEFAULT VALUE


