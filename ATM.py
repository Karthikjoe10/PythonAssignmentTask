
class ATM:

    def __init__(self):
        self.balance = 10000
        self.pin = "1234"

    # Check balance
    def check_balance(self):
        print("Current balance: ₹", self.balance)

    # Deposit money
    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount <= 0:
                print("Please enter a valid amount!")
            else:
                self.balance += amount
                print("Deposit successful!")
                print("Current balance: ₹", self.balance)

        except ValueError:
            print("Invalid input! Enter numbers only.")

    # Withdraw money
    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Please enter a valid amount!")

            elif amount > self.balance:
                print("Insufficient balance!")

            else:
                self.balance -= amount
                print("Withdrawal successful!")
                print("Current balance: ₹", self.balance)

        except ValueError:
            print("Invalid input! Enter numbers only.")

    # ATM menu
    def menu(self):

        attempts = 0

        # PIN verification
        while attempts < 3:
            entered_pin = input("Enter your ATM PIN: ")

            if entered_pin == self.pin:
                print("\nLogin successful!")
                break
            else:
                attempts += 1
                print("Incorrect PIN!")

        if attempts == 3:
            print("Your ATM access is blocked!")
            return

        # Display menu repeatedly
        while True:

            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            try:
                choice = int(input("\nEnter choice: "))

                if choice == 1:
                    self.check_balance()

                elif choice == 2:
                    self.deposit()

                elif choice == 3:
                    self.withdraw()

                elif choice == 4:
                    print("Thank you for using ATM!")
                    break

                else:
                    print("Invalid choice! Please select 1 to 4.")

            except ValueError:
                print("Invalid input! Enter a number.")


# Main program
atm = ATM()
atm.menu()
