import datetime

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer name:", self.customer_name)
        print("Account number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print("Current balance:", self.balance)
account = BankAccount("904356789", 34500, datetime.date.today(), "lewis nyabuto")

print(account.deposit(1000))   
print(account.withdraw(2000)) 
account.check_balance()        
account.customer_details()   