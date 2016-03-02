class Employee(object):
    def __init__(self, fname, lname, grade):
        self.fname = fname
        self.lname = lname
        self.grade = grade

    def __str__(self):
        return "Employee [First Name: %s, Last Name: %s, grade = %d" \
            % (self.fname, self.lname, self.grade)
