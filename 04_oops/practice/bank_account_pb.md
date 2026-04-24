# Bank Account System

## Question 0: Class for Bank Account

```
Design a Python class named `BankAccount` to represent bank accounts.

Theory:
A bank account typically includes attributes such as account number, balance, and account holder name.

The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts.

Operations:

1. Deposit:
   Add funds to the account

2. Withdrawal:
   Subtract funds from the account

3. Transfer:
   Transfer funds from one account to another

Test Cases:

Test Case 1:
acc1 = BankAccount("John Doe", 1000)
acc2 = BankAccount("Jane Smith", 2000)

assert acc1.balance == 1000
assert acc2.balance == 2000

acc1.deposit(500)
acc2.withdraw(100)
acc1.transfer(acc2, 200)

assert acc1.balance == 1300
assert acc2.balance == 2300


Test Case 2:
acc3 = BankAccount("Alice Johnson", 500)
acc4 = BankAccount("Bob Brown", 1500)

assert acc3.balance == 500
assert acc4.balance == 1500

acc3.deposit(100)
acc4.withdraw(200)
acc3.transfer(acc4, 300)

assert acc3.balance == 400
assert acc4.balance == 1800
```
