#!/usr/bin/env python

# bytearray([x])

# A type representing a mutable array of bytes. When creating an instance,
# x may be an iterable sequence of integers in the range 0 to 255,
# an 8-bit string or bytes literal, or an integer that specifies the size
# of the array (in which case every entry will be initialized to 0).

# Initialized with 32 zero bytes
a = bytearray(32)

# Copy individual characters from the word "Hello" to a, starting at index 0.
for i, c in enumerate("Hello"):
    a[i] = c

# Prints "Hello"
print a

# bump i, since it points to the index of last character from the preceding loop
i += 1

# assign individual character past the string "Hello"
a[i] = ' '
i += 1

# Replace a 1-byte slice at [i] with "World
a[i:i] = "World"

# Prints "Hello World"
print a

# Pure strings also seem to work, but it's suggested to prefix string literals i
# with b while working with bytearrays, to indicate we're operating on bytes
searchstr = b"World"        
replacestr = b"Stranger"

if a.find(searchstr) != -1:
    print "Found '%s' -- replacing with '%s'" % (searchstr, replacestr)
    a = a.replace(searchstr, replacestr)        # a.replace() returns a *copy* of a!
    print a
