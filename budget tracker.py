import pickle
import datetime

class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

# Loads transactions form a file
# Returns an empty list if the file does not exist
def load_transactions(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

# Saves the current list of transactions to a file
def save_transactions(filename, transactions):
    with open(filename, 'wb') as f:
        pickle.dump(transactions, f)

# Adds a new transaction after getting user input
def add_transaction(transactions, filename):
    print()
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    description = input("Enter description: ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    
    transactions.append(Transaction(date, description, amount))
    save_transactions(filename, transactions)

# Displayes all recorded transactions
def view_transactions(transactions):
    print()
    print("-" * 30)
    print("Transactions:")
    print("-" * 30)
    for transaction in transactions:
        print(f"{transaction.date} | {transaction.description:<20} | ${transaction.amount:8.2f}")

# Calculates and returns the current balance base on transactions
def get_balance(transactions):
    return sum(transaction.amount for transaction in transactions)

# Clears all transactions from the list and the file
def clear_history(transactions, filename):
    transactions.clear() # Clears the list of all transactions
    save_transactions(filename, transactions) # Saves the empyt list
    print("Transaction history cleared.")

if __name__ == "__main__":
    filename = "transactions.dat"
    transactions = load_transactions(filename)
    
    while True:
        print()
        print("=" * 30)
        print("Menu:")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Get balance")
        print("4. Clear transaction history")
        print("5. Exit")
        print("=" * 30)
        
        print()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_transaction(transactions, filename)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            balance = get_balance(transactions)
            print(f"Current balance: ${balance:.2f}")
        elif choice == "4":
            clear_history(transactions, filename)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
