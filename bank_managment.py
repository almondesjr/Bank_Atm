from classes import Account, Bank
import time

def main():
    bank = Bank()

    while True:
        print("Bank Management System")
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1: #create account
            account_number = input("\nInput 6 numbers to become your account number: ")
            if len(account_number) == 6 and account_number.isdigit():
                print("Valid account_number")
            else:
                print("Invalid account number try again.")
            
            account_holder = input("Enter account holder name: ")
            if account_holder.isalpha(): #checks to see if meets requierment 
                print("Valid account holder name")
            else:
                print("Invalid account holder name. Please enter only letters.")

            while True: #checks to see if length meet requierment 
                pin = input("Set a PIN for this account\nPIN must only contain 4 to 6 numbers: ")
                if pin.isdigit() and 4 <= len(pin) <= 6:
                    break
                else:
                    print("Invalid PIN format. Please enter 4 to 6 digits.")

            initial_balance = float(input("Enter initial balance: "))

            print("\nSelect your account type:")
            print("1. Checking account")
            print("2. Savings account")
            account_type = int(input("Enter your choice "))
            
            #Choose account type
            if account_type == 1:
                account = bank.create_account(account_number, account_holder, pin, initial_balance, account_type = "checking")
                print("\nChecking account created successfully.")
            elif account_type == 2:
                account = bank.create_account(account_number, account_holder, pin, initial_balance, account_type = "savings")
                print("\nSavings account created successfully.")
            else:
                print("\nInvalid choice")
                
        elif choice == 2:  # Deposit
            account_number = input("\nEnter account number: ")
            account = bank.get_account(account_number)
            
            if isinstance(account, Account):
                if account.verify_pin():
                    print("\nSelect deposit type:")
                    print("1. Cash")
                    print("2. Check")
                    deposit_choice = int(input("Enter your choice: "))
                    
                    #Choose type
                    if deposit_choice == 1:
                        deposit_amount = float(input("\nEnter cash deposit amount: "))
                        print(account.deposit(deposit_amount))
                    elif deposit_choice == 2:
                        deposit_amount = float(input("\nEnter check deposit amount: "))
                        print(account.deposit(deposit_amount))
                    else:
                        print("Invalid deposit type")
                else:
                    print("Invalid PIN or account number")
            else:
                print("Invalid account number")
      
        elif choice == 3:  # Withdraw
            account_number = input("\nEnter account number: ")
            account = bank.get_account(account_number)
            
            if isinstance(account, Account):
                if account.verify_pin():
                    account.reset_daily_withdrawal()
                else:
                    print("Invalid account number or PIN")

                amount = float(input("\nEnter withdrawal amount: "))

                if amount < 0:
                    print("Invalid amount")
                elif amount % 100 != 0:
                    print("Withdrawal amount must be in multiples of 100 (dollars)")
                elif account.daily_withdrawal_total + amount > 1000:
                    print("Daily withdrawal limit exceeded")
                else: #denominations
                    num_hundreds = amount // 100
                    num_fifties = (amount % 100) // 50
                    num_twenties = ((amount % 100) % 50) // 20
                    num_tens = (((amount % 100) % 50) % 20) // 10

                    print("Withdrawl details")
                    print(f"100s: {num_hundreds}")
                    print(f"50s: {num_fifties}")
                    print(f"20s: {num_twenties}")
                    print(f"10s: {num_tens}")

                    print(account.withdraw(amount))

                    #update daily amount count
                    account.daily_withdrawal_total += amount
            else:
                print("Invalid account number or PIN")

        elif choice == 4:  # Check Balance
            account_number = input("\nEnter account number: ")
            account = bank.get_account(account_number)

            if isinstance(account, Account):
                if account.verify_pin():
                    print(account.get_balance())
            else:
                print("Invalid account number or PIN")

        elif choice == 5:  # Transfer Balance
            source_account_number = input("\nEnter your account number: ")
            source_account = bank.get_account(source_account_number)
            
            if isinstance(source_account, Account):
                if source_account.verify_pin():
                    destination_account_number = input("\nEnter destination account number: ")
                    transfer_amount = float(input("Enter transfer amount: "))
                    destination_account = bank.get_account(destination_account_number)
                    
                    #Provide details
                    if isinstance(destination_account, Account):
                        print("\nTransfer details:")
                        print(f"From: {source_account.account_number} ({source_account.account_holder})")
                        print(f"To: {destination_account_number} ({destination_account.account_holder})")
                        print(f"Amount: ${transfer_amount:.2f}")
                        
                        confirm = input("\nAre you sure you want to proceed?\n 1.Yes\n 2.No\n Enter your choice (yes/no): ").lower()
                        if confirm == "1":
                            transfer_result = source_account.transfer_funds(destination_account, transfer_amount)
                            print(transfer_result)
                        elif confirm == "2":
                            print("\nTransferd cancled")
                        else:
                            print("\nInvalid Choice")
                    else:
                        print("\nDestination account not found.")
                else:
                    print("\nInvalid PIN")
            else:
                print("\nSource account not found.")
            
        elif choice == 6:# Quit program, display, thank you message
            print("\nThank you for banking with us, take care!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

        time.sleep(2)

if __name__ == "__main__":
    main()
