#!/bin/python3

def cut():
    print "----------------"

# List assignment
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for i in l:         # iterating and fetching items into a control variable
    sum += i
print "Sum of numbers %d to %d equals: %d" % (l[0], l[-1], sum)
                                            #   ^      ^------ Stands for <LIST LENGTH - 1>, i.e. the index of the last element
                                            #   |------------- List indexes are zero-based
cut()

# We can iterate through a list as follows
print "List contents: values only"
for item in l:
    print item;
cut()

# We can iterate through a list as follows
print "List contents: index - value"
for i in range(0,len(l)):
    print "index %2d: value = %2d" % (i, l[i])
cut()

# Appending to list
print "Appending to list" 
l.append(11)
print l 
cut()

# Inserting to list
print "Inserting to list"
l.insert(2, "Inserted item")    # Note, we can mix items of ANY TYPE in a single list!
print l
cut()

# Slicing
print "Slicing"
print "[0:2] ", l[0:2]
print "[2:]  ", l[2:]
cut()

# Concatenating
a = [1, 2, 3] + [4, 5]

# These create an empty list
names = []
names = list()

# Lists can contain any kind of Python object, including other lists:
a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
print "Mixed list: a =",
print a;
print "a[1] =", a[1]               # Returns "Dave"
print "a[3][2] =", a[3][2]         # Returns 9
print "a[3][3][1] =", a[3][3][1]   # Returns 101
cut
