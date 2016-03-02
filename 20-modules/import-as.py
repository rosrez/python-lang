#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print "Usage import-as.py <filename> <upper|lower"
    raise SystemExit(1)

filename = sys.argv[1]
mode = sys.argv[2]

# Conditionally import either module under the same name (processor)
# If the modules provide the same API, we can use the API
# seamlessly after import

if mode == "lower":
    import processor_lower as processor
elif mode == "upper":
    import processor_upper as processor
else:
    print "Unsupported mode: %s" % mode
    raise SystemExit(2)

for l in open(filename):
    print processor.process(l),
