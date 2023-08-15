# Bank_Atm
Your project is a simple command-line Bank Management System implemented in Python using classes and functions. The system allows users to perform various banking operations such as creating accounts, depositing funds, withdrawing funds, checking account balances, and transferring funds between accounts. Here's a breakdown of the main components and functionalities:

1. **Import Statements:**
   - The project starts by importing the necessary classes `Account` and `Bank` along with the `time` module.

2. **Main Function (`main`):**
   - The main function is the entry point of the program.
   - It creates an instance of the `Bank` class to manage accounts and operations.

3. **Menu Loop:**
   - The program enters an infinite loop, displaying a menu of available banking operations.
   - Users can choose an option from the menu by entering a numeric choice.

4. **Account Creation (`choice == 1`):**
   - Users can create a new account by providing an account number, account holder name, PIN, initial balance, and account type (checking or savings).
   - Validation checks are performed on user inputs for account number, account holder name, PIN format, and account type.

5. **Deposit Funds (`choice == 2`):**
   - Users can deposit funds into an existing account by providing the account number and PIN for verification.
   - Users choose the deposit type (cash or check) and enter the deposit amount.
   - Appropriate validations and operations are performed on the account.

6. **Withdraw Funds (`choice == 3`):**
   - Users can withdraw funds from an existing account after PIN verification.
   - Validation is done for withdrawal amount, ensuring it's in multiples of 100.
   - The withdrawal amount is divided into denominations of 100s, 50s, 20s, and 10s, and details are displayed.

7. **Check Balance (`choice == 4`):**
   - Users can check the account balance after PIN verification.

8. **Transfer Funds (`choice == 5`):**
   - Users can transfer funds from one account to another.
   - Source and destination accounts are verified by PIN.
   - Users provide transfer details, including the transfer amount, and can confirm the transfer.

9. **Exit (`choice == 6`):**
   - Users can exit the program, displaying a thank you message.

10. **Validation and User Interaction:**
    - Throughout the program, various input validations are performed to ensure proper user input.
    - User choices and inputs are captured using the `input` function, and outputs are displayed using the `print` function.
    
11. **Sleep Timer:**
    - After each operation, there's a pause of 2 seconds to provide a smoother user experience.

The project demonstrates fundamental programming concepts such as classes, object instantiation, conditional statements, loops, input/output operations, and basic error handling. It provides users with a basic interface to interact with a simple banking system through the command line.
