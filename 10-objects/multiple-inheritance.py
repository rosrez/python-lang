#!/usr/bin/env python

# Instance vs class methods 

class Account(object):
    num_accounts = 0

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

# A mixin class: a piece of specific functionality to collect deposit charge

class DepositCharge(object):
    fee = 5.00
    def deposit_fee(self):
        # We cannot use self.withdraw() since we are being called from it;
        # this would result in an infinite recursion.
        # This is why we use the superclass's withdraw() method.
        # Also, avoid using self.fee, it's ambiguous if we inherit from both mixin classes
        super(ChargedAccount, self).withdraw(DepositCharge.fee)

# A mixin class: a piece of specific functionality to collect withdraw charge

class WithdrawCharge(object):
    fee = 2.50
    def withdraw_fee(self):
        # We cannot use self.withdraw() since we are being called from it;
        # this would result in an infinite recursion.
        # This is why we use the superclass's withdraw() method.
        # Also, avoid using self.fee here, it's ambiguous if we use multiple inheritance
        super(ChargedAccount, self).withdraw(WithdrawCharge.fee)

# A class that uses multiple inheritance to enhance the class tree with

class ChargedAccount(Account, DepositCharge, WithdrawCharge):
    def __init__(self, name, balance):
        Account.__init__(self, name, balance)

    def deposit(self, amt):
        self.deposit_fee()                          # self supplied to method implicitly
        super(ChargedAccount, self).deposit(amt) 

    def withdraw(self, amt):
        self.withdraw_fee()
        super(ChargedAccount, self).withdraw(amt)   # self supplied to method implicitly

# Create an instance of class Account
a = Account("Guido", 1000.00)       # invokes Account.__init__(a, "Guido", 1000.00)
print "Account a = %s, instance count = %d" % (a, Account.num_accounts)
a.deposit(100.00)
print "Deposited 200.00 to a: %s" % a
a.withdraw(200.00)
print "Withdrawn 100.00 from a: %s" % a

# Create an instance of class ChargedAccount
c = ChargedAccount("Chris", 10.00)
print "Account c = %s, instance count = %d" % (c, Account.num_accounts)
c.deposit(200.00)
print "Deposited 200.00 to c: %s" % c
c.withdraw(100.00)
print "Withdrawn 100.00 from a: %s" % c
