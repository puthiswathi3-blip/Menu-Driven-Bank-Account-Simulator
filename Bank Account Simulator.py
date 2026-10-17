
# Menu-Driven Bank Account Simulator

balance = 0.0
transactions = []


def check_balance():
    """Display the current account balance."""
    print(f"\nCurrent Balance: Rs. {balance:.2f}")


def deposit():
    """Add money to the account."""
    global balance

    try:
        amount = float(input("Enter amount to deposit: Rs. "))

        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            balance += amount
            transactions.append(f"Deposited: Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} deposited successfully.")
            print(f"Updated Balance: Rs. {balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


def withdraw():
    """Withdraw money if sufficient balance is available."""
    global balance

    try:
        amount = float(input("Enter amount to withdraw: Rs. "))

        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} withdrawn successfully.")
            print(f"Remaining Balance: Rs. {balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


def transaction_history():
    """Display all successful transactions."""
    print("\n----- Transaction History -----")

    if not transactions:
        print("No transactions available.")
    else:
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction}")

    print("--------------------------------")


def main():
    """Display the menu and handle user choices."""
    while True:
        print("\n===== BANK ACCOUNT SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you for using the Bank Account Simulator!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
