from tracker import FinanceTracker
from models import Transaction
from storage import save_data, load_data
from exceptions import (
    InvalidAmountError,
    InvalidCategoryError,
    TransactionNotFoundError,
    InsufficientFundsError
)

def test_add_income():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Monthly salary")
    assert tracker.balance == 5000
    assert tracker.total_income == 5000
    print("✅ test_add_income passed")

def test_add_expense():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Salary")
    tracker.add_transaction("expense", 800, "food", "2024-01-16", "Groceries")
    assert tracker.balance == 4200
    assert tracker.total_expenses == 800
    print("✅ test_add_expense passed")

def test_insufficient_funds():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 1000, "salary", "2024-01-15", "Salary")
    try:
        tracker.add_transaction("expense", 5000, "rent", "2024-01-16", "Rent")
        print("❌ test_insufficient_funds FAILED — should have raised")
    except InsufficientFundsError:
        print("✅ test_insufficient_funds passed")

def test_invalid_amount():
    tracker = FinanceTracker()
    try:
        tracker.add_transaction("income", -500, "salary", "2024-01-15", "Bad amount")
        print("❌ test_invalid_amount FAILED")
    except InvalidAmountError:
        print("✅ test_invalid_amount passed")

def test_get_by_category():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Salary")
    tracker.add_transaction("expense", 800, "food", "2024-01-16", "Groceries")
    tracker.add_transaction("expense", 300, "food", "2024-01-17", "Dinner")
    results = tracker.get_by_category("food")
    assert len(results) == 2
    print("✅ test_get_by_category passed")

def test_remove_transaction():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Salary")
    tracker.remove_transaction("T001")
    assert len(tracker._transactions) == 0
    print("✅ test_remove_transaction passed")

def test_remove_nonexistent():
    tracker = FinanceTracker()
    try:
        tracker.remove_transaction("T999")
        print("❌ test_remove_nonexistent FAILED")
    except TransactionNotFoundError:
        print("✅ test_remove_nonexistent passed")

def test_monthly_summary():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Salary")
    tracker.add_transaction("expense", 800, "food", "2024-01-16", "Groceries")
    tracker.add_transaction("income", 2000, "salary", "2024-02-01", "Bonus")
    summary = tracker.monthly_summary(1, 2024)
    assert summary["income"] == 5000
    assert summary["expenses"] == 800
    print("✅ test_monthly_summary passed")

def test_save_and_load():
    tracker = FinanceTracker()
    tracker.add_transaction("income", 5000, "salary", "2024-01-15", "Salary")
    tracker.add_transaction("expense", 800, "food", "2024-01-16", "Groceries")
    save_data(tracker, "test_data.json")
    loaded = load_data("test_data.json")
    assert len(loaded) == 2
    assert loaded[0].amount == 5000
    assert loaded[1].category == "food"
    print("✅ test_save_and_load passed")

def test_to_dict_from_dict():
    t = Transaction("T001", "income", 5000, "salary", "2024-01-15", "Salary")
    d = t.to_dict()
    t2 = Transaction.from_dict(d)
    assert t2.transaction_id == "T001"
    assert t2.amount == 5000
    assert t2.category == "salary"
    print("✅ test_to_dict_from_dict passed")


if __name__ == "__main__":
    print("Running all tests...\n")
    test_add_income()
    test_add_expense()
    test_insufficient_funds()
    test_invalid_amount()
    test_get_by_category()
    test_remove_transaction()
    test_remove_nonexistent()
    test_monthly_summary()
    test_save_and_load()
    test_to_dict_from_dict()
    print("\nAll tests complete.")