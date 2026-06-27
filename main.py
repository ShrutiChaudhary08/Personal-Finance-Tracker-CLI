"""Command-line interface for the Personal Finance Tracker.
Entry point for user interaction with the application.
"""
from tracker import FinanceTracker
from storage import save_data, load_data
from exceptions import (
    InvalidAmountError,
    InvalidCategoryError,
    TransactionNotFoundError,
    InsufficientFundsError,
    FileProcessingError
)

FILEPATH = "data.json"

def show_menu() -> None:
    print("\n" + "=" * 40)
    print("   PERSONAL FINANCE TRACKER")
    print("=" * 40)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance & Summary")
    print("4. View by Category")
    print("5. Monthly Summary")
    print("6. Remove Transaction")
    print("7. Save & Exit")
    print("=" * 40)

def add_transaction(tracker: FinanceTracker, transaction_type: str) -> None:
     """Handles adding either income or expense."""
     try:
        amount = float(input("Amount: ₹"))
        print("Categories:", ", ".join([
            "salary", "food", "rent", "transport",
            "entertainment", "health", "savings", "other"
        ]))
        category = input("Category: ").strip().lower()
        date = input("Date (YYYY-MM-DD): ").strip()
        description = input("Description: ").strip()

        tracker.add_transaction(transaction_type, amount, category, date, description)

     except InvalidAmountError as e:
        print(f"Invalid amount: {e}")
     except InvalidCategoryError as e:
        print(f"Invalid category: {e}")
     except InsufficientFundsError as e:
        print(f"Insufficient funds: {e}")
     except ValueError:
        print("Amount must be a number.")

def view_summary(tracker: FinanceTracker) -> None:
    print(tracker)

def view_by_category(tracker: FinanceTracker) -> None:
    try:
        category = input("Enter category: ").strip().lower()
        results = tracker.get_by_category(category)
        if not results:
            print(f"No transactions found for '{category}'.")
        else:
            print(f"\n--- Transactions in '{category}' ---")
            print(results)
    except InvalidCategoryError as e:
        print(f"Error: {e}")

def remove_transaction(tracker: FinanceTracker) -> None:
    try:
        transaction_id = input("Enter transaction ID to remove: ").strip().upper()
        tracker.remove_transaction(transaction_id)
    except TransactionNotFoundError as e:
        print(f"Error: {e}")

def main() -> None:
    tracker = FinanceTracker()

    # load existing data on startup
    try:
        transactions = load_data(FILEPATH)
        tracker._transactions = transactions
        if transactions:
            print(f"Loaded {len(transactions)} transactions from file.")
    except FileProcessingError as e:
        print(f"Warning: Could not load data. Starting fresh. Reason: {e.reason}")
while True:
     show_menu()
     choice = input("Choose option (1-7): ").strip()

     if choice == "1":
          add_transaction(FinanceTracker, "income")
     elif choice == "2":
          add_transaction(FinanceTracker, "expense")
     elif choice == "3":
          view_summary(FinanceTracker)
     elif choice == "4":
          view_by_category(FinanceTracker)
     elif choice == "5":
          view_summary(FinanceTracker)
     elif choice == "6":
          remove_transaction(FinanceTracker)
     elif choice == "7":
          try:
               save_data(FinanceTracker, FILEPATH)
               print("Data saved. Goodbye.")
          except FileProcessingError as e:
                print(f"Could not save: {e}")
          break
     else:
          print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()