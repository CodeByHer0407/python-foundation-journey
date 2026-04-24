class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amt):
        if amt <= 0:
            print("Withdrawal amount must be positive")
        elif amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt

    def transfer(self, other_accout, amt):
        if amt <= 0:
            print("Transfer amount must be positive")
        elif amt > self.balance:
            print("Insufficient balance for transfer")
        else:
            self.withdraw(amt)
            other_accout.deposit(amt)

    def __str__(self):
        return f"Bank Account Holder: {self.account_holder}, Available Balance: {self.balance}"  


acc1 = BankAccount("John Doe", 1000)
acc2 = BankAccount("Jane Smith", 2000)

print(acc1)
print(acc2)
assert acc1.balance == 1000
assert acc2.balance == 2000

acc1.deposit(500)
acc2.withdraw(100)

print(acc1)
print(acc2)

acc1.transfer(acc2, 200)
print(acc1)
print(acc2)

assert acc1.balance == 1300
assert acc2.balance == 2300