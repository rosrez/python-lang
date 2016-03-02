#!/usr/bin/env python

# Demo of persisting objects in a file

import pickle
from employee import Employee

filename = "employee.out"

e1 = Employee("John", "Doe", 7)
e2 = Employee("Jane", "Doe", 8)

f = open(filename, 'wb')        # opens file for binary output (important for portability, e.g. to Windows)
pickle.dump(e1, f)              # save object in f
pickle.dump(e2, f)              # save object in f
f.close()
