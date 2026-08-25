# Banking System using PEAS Representation

class Bank:

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

        # PEAS Representation
        self.performance = "Correct Transactions, Secure Banking, Accurate Balance"
        self.environment = "Customer, Bank Database, Banking System"
        self.actuators = ["Display Balance", "Deposit Money", "Withdraw Money"]
        self.sensors = ["Username", "PIN", "Deposit Amount", "Withdraw Amount"]

    # Display PEAS
    def display_peas(self):
        print("===== PEAS Representation =====")
        print("Performance Measure :", self.performance)
        print("Environment         :", self.environment)
        print("Actuators           :", ", ".join(self.actuators))
        print("Sensors             :", ", ".join(self.sensors))
        print()

    # Check Balance
    def check_balance(self, name, pin):
        if self.name == name and self.pin == pin:
            print("Your Balance is Rs.", self.balance)
        else:
            print("Invalid Username or PIN")

    # Deposit Money
    def deposit(self, name, pin, amount):
        if self.name == name and self.pin == pin:
            self.balance += amount
            print("Deposit Successful! Rs.", amount)
            print("Current Balance: Rs.", self.balance)
        else:
            print("Invalid Username or PIN")

    # Withdraw Money
    def withdraw(self, name, pin, amount):
        if self.name == name and self.pin == pin:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successful! Rs.", amount)
                print("Remaining Balance: Rs.", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Username or PIN")


# Create Bank Account
account = Bank("md_belal", 123456, 3000)

# Check Balance
account.check_balance("md_belal", 123456)

# Deposit Rs. 5000
account.deposit("md_belal", 123456, 5000)

# Withdraw Rs. 700
account.withdraw("md_belal", 123456, 700)

# Final Balance
account.check_balance("md_belal", 123456)


account.display_peas()
