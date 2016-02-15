#!/usr/bin/env python

s2 = set(range(2,61,2))
s3 = set(range(3,61,3))

print "Set of numbers divisible by 2 (S2)"
print s2
print "Set of numbers divisible by 3 (S3)"
print s3



union = list(s2 | s3)
intersect = list(s2 & s3)
diff = list(s2 - s3)
symdiff = list(s2 ^ s3)

# Note that sort() performs the sorting IN-PLACE,
# so the result of sorting be available during evaluation of
# complex expressions that include sort().
# This is why we sort the items explicitly as a separate step

union.sort()
intersect.sort()
diff.sort()
symdiff.sort()

print "Union (S2 | S3):\n", union 
print "Intersection (S2 & S3):\n", intersect 
print "Set difference (S2 - S3):\n", diff
print "Symmetric difference (S2 ^ S3):\n", symdiff

