#/usr/bin/env python
# P2

principal = 1000        # Initial amount (int, initially)
rate = 0.05             # Interest rate (float)
numyears = 5            # Number of years
year = 1
while year <= numyears:
    principal = principal * (1 + rate)          # principal is now float
    print "%3d %0.2f" % (year, principal)
    # print("%3d %0.2f" % (year, principal))    # Python 3
    year += 1
