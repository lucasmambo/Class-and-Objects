class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance ({self.balance}) to withdraw {amount} from account {self.account_number}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}")

    def check_balance(self):
        print(f"Balance for account {self.account_number} is {self.balance}")

    def customer_details(self):
        print(f"Account number: {self.account_number}")
        print(f"Customer name: {self.customer_name}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")
account = BankAccount("12345", 10000, "18th June 2019", "Lucas Mambo")
account.customer_details()
account.deposit(6000)
account.check_balance()
account.withdraw(2000)
account.check_balance()