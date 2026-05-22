# Exercice 1: Bank Account


class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated. Please log in.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated. Please log in.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated. Please log in.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(
                f"Cannot withdraw. Balance would fall below minimum balance of {self.minimum_balance}."
            )
        self.balance -= amount


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list")
        for acc in account_list:
            if not isinstance(acc, (BankAccount, MinimumBalanceAccount)):
                raise Exception(
                    "All items in account_list must be BankAccount or MinimumBalanceAccount instances"
                )
        self.account_list = account_list

        try:
            if try_limit > 0:
                self.try_limit = try_limit
            else:
                self.try_limit = 2
        except:
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.log_in()
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")

    def log_in(self):
        while self.current_tries < self.try_limit:
            username = input("Username: ")
            password = input("Password: ")
            for account in self.account_list:
                if account.authenticate(username, password):
                    print("Login successful!")
                    self.current_tries = 0
                    self.show_account_menu(account)
                    return
            self.current_tries += 1
            remaining = self.try_limit - self.current_tries
            print(
                f"Invalid credentials. Attempt {self.current_tries} of {self.try_limit}. {remaining} attempts left."
            )
        print("Maximum login attempts reached. Shutting down.")
        exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu for {account.username} ---")
            print(f"Balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                try:
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposited {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Returning to main menu.")
                break
            else:
                print("Invalid option.")


# Exemple d'utilisation (tests)
if __name__ == "__main__":
    acc1 = BankAccount(1000, "alice", "pass123")
    acc2 = MinimumBalanceAccount(500, "bob", "pass456", minimum_balance=100)

    atm = ATM([acc1, acc2], try_limit=3)
