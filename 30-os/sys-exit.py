#!/usr/bin/env python

# The scripts sole job is to exit with a user-provided exit code 
# (0 is assumed by default).

# sys.exit([n])
# Exits Python by raising the SystemExit exception. n is an integer code
# indicating a status code.
# If a noninteger value is given to n, it's printed to sys.stderr
# and an exit code of 1 is used.

import sys

exitcode = 0
if len(sys.argv) > 1:
    # convert to int, otherwise sys.argv[1] gets printed on the console
    # even if it contains a number; also, 1 will be returned instead
    # of the intended error code
    exitcode = int(sys.argv[1]) 
sys.exit(exitcode)
