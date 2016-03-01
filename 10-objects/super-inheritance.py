#!/usr/bin/env python

# Instance vs class methods 

class Account(object):
    num_accounts = 0                    # class variable; defined within a class

    # This is __init__() that defines instance variables. Assignments such as
    # self.name = adds key-value pairs to the underlying dictionary 
    # that stores all the field names and values. The very same dictionary stores
    # method objects for the class, so methods like __init__(), __del()__ or
    # deposit() also end up there

    # the constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1       # count instances: operates on Account class instead of instance

    # implicitly called by print
    def __str__(self):
        return "[ %s -- balance is %.2f ]" % (self.name, self.balance)

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def inquiry(self):
        return self.balance

# super(cls, instance) returns an ancestor object for this class
# so we can call an instance method on it.

# Alternatively, we can explicitly specify the name of the base class
# along with the method, as in Account.__init__() invocation.

# Note the difference between invocations in the derived class:
#
# Account.deposit(self, amt), and
#
# super(ChargedAccount, self).deposit(amt)
#                                     ^----- self IS NO LONGER REQUIRED

class ChargedAccount(Account):
    def __init__(self, name, balance, charge):
        Account.__init__(self, name, balance)
        self.charge = charge

    def deposit(self, amt):
        self.withdraw(self.charge)                              # collect a charge first (calls ancestor method)
        super(ChargedAccount,self).deposit(amt)           # super().deposit(self, amt) in Python 3

# Create a few instances of class Account
a = Account("Guido", 1000.00)       # invokes Account.__init__(a, "Guido", 1000.00)
print "Account a = %s, instance count = %d" % (a, Account.num_accounts)
a.deposit(100.00)
print "Withdrawn 100.00 from a: %s" % a

b = Account("Bill", 10.00)
print "Account b = %s, instance count = %d" % (b, Account.num_accounts)
b.deposit(100.00)
print "Deposited 100.00 to b: %s" % b

c = ChargedAccount("Chris", 10.00, 5.00)
print "Account b = %s, instance count = %d" % (c, Account.num_accounts)
c.deposit(100.00)
print "Deposited 100.00 to b: %s" % b
