"""
    main.py
"""

import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456, account_firstname="Royce",
                              account_lastname="Chua", current_balance=1000,
                              address="Silver Street Quezon City",
                              email="roycechua123@gmail.com")
                            # whenever we make an object, we have 'ingredients' that we need
                            # in Python, the ingredients are the parameters in 'constructor' __init__
                            # we do not need to pass self when calling for a method (Python assumes it is there)

print("Account 1") 

# this code block is basically just checking whether the attributes we assigned worked
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print() # this is just a space, don't overthink lol

Account2 = Accounts.Accounts(account_number=654321, account_firstname="John",
                              account_lastname="Doe", current_balance=2000,
                              address="Gold Street Quezon City",
                              email="johndoe@yahoo.com")

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

print()

# Creating and Using an ATM object
 
ATM1 = ATM.ATM(account=Account1) # syntax is Filename.Classname(), we are creating an object (ATM) with the name ATM1

ATM1.deposit(Account1, 500) # in ATM.py, the functions take in account and amount
ATM1.check_currentbalance(Account1)

ATM1.deposit(Account2, 300)
ATM1.check_currentbalance(Account2)

ATM1.view_transactionsummary()
ATM1.print_serial_number()