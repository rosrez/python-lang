#!/usr/bin/python2

filename = "../txt/employees.csv"
employees = []
for line in open(filename):
    fields = line.split(',')            # Split each line into a list
    name = fields[0]                    # Extract and convert individual fields
    grade = fields[1]
    salary = float(fields[2])
    person = (name, grade, salary)      # Create a tuple out of individual fields
    employees.append(person)            # Add tuple to list of records

max = 0
for name, grade, salary in employees:
    if max < salary:
        max, mname = salary, name       # Without parentheses, tuples are assumed automatically

print "{0} earns the maximum salary of {1:0.2f}".format(mname, max)
