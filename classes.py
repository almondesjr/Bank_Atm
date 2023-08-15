class Account:
    def __init__(self, account_number, account_holder, pin, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.daily_withdrawal_total = 0 # Initialize daily withdrawal total to zero

    def reset_daily_withdrawal(self):
        self.daily_withdrawal_total = 0 # Reset daily withdrawl total to zero

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance"

    def get_balance(self):
        return f"Account balance: {self.balance}"
    
    def transfer_funds(self, destination_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            destination_account.deposit(amount)
            return "Funds transferred successfully"
        
        else:
            return "Insufficient funds for transfer"
        
    def verify_pin(self):
        pin_attempts = 0
        while pin_attempts < 3:
            pin = input("Enter PIN: ")
            if self.pin == pin:
                print("Login successful.")
                return True
            else:
                pin_attempts += 1
                remaining_attempts = 3 - pin_attempts
                if remaining_attempts > 0:
                    print(f"Invalid PIN. You have {remaining_attempts} attempts remaining.")
                else:
                    print("Invalid PIN. Exiting the program.")
                    exit()
        return False
        
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, pin, balance=0):
        super().__init__(account_number, account_holder, pin, balance)
        self.account_type = "Checking" # Set account type to "Checking"

    def __str__(self):
        return f"Checking Account #{self.account_number}"
    
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, pin, balance=0):
        super().__init__(account_number, account_holder, pin, balance)
        self.account_type = "Savings" # Set account type to "Savings"

    def __str__(self):
        return f"Savings Account #{self.account_number}"

class Bank:
    def __init__(self):
        self.accounts = [] # Initialize an empty list to store accounts

    def create_account(self, account_number, account_holder, pin, initial_balance, account_type):
        if account_type == "checking":
            new_account = CheckingAccount(account_number, account_holder, pin, initial_balance)
            self.accounts.append(new_account) # Add the new account to the accounts list
            return "Checking account created successfully."
        elif account_type == "savings":
            new_account = SavingsAccount(account_number, account_holder, pin, initial_balance)
            self.accounts.append(new_account) # Add the new accountt to the accounts list
            return "Savings account created successfully."
        else:
            return "Invalid account type"

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None  # Return None if account is not found
