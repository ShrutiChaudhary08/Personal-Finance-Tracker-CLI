# Correct
from models import Transaction, Valid_Categories, Valid_Types  
from exceptions import (                                          
    FinanceError,
    InvalidAmountError,
    InvalidCategoryError,
    TransactionNotFoundError,
    InsufficientFundsError
)

class FinanceTracker:
    """This class stores the list of Transaction objects."""
    def __init__(self):
        self._transactions: list[Transaction]=[]   # A list of Transaction objects

   
    @property  
    def total_income(self) -> float:
        total=0.0
        for transaction in self._transactions:
            if transaction.type=="income":
                total+=transaction.amount
        return total

    
    @property
    def total_expenses(self) -> float:
       total=0.0
       for transaction in self._transactions:
           if transaction.type=="expense":
               total+=transaction.amount
       return total

    @property
    def balance(self) -> float:
       return self.total_income-self.total_expenses
       
    
    def add_transaction(self, type: str, amount: float, category: str, date: str, description: str) -> None:    # validates, creates Transaction, appends
        transaction_id = f"T{len(self._transactions) + 1:03d}"

        new_transaction=Transaction(
            transaction_id,
            type, 
            amount, 
            category, 
            date, 
            description)


        if type.lower() == "expense" and amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        
        self._transactions.append(new_transaction)
        

    
    def get_by_category(self, category: str) -> list[Transaction]:
        # returns filtered list
        if category.lower() not in Valid_Categories:
            raise InvalidCategoryError(category)
        return [t for t in self._transactions if t.category == category.lower()]

    
    def remove_transaction(self, transaction_id: str) -> None:
        for transaction in self._transactions:
            if transaction.transaction_id==transaction_id:
                self._transactions.remove(transaction)
                return
        raise TransactionNotFoundError(transaction_id)
        

    def monthly_summary(self, month: int, year: int) -> dict:
        month_prefix=f"{year}-{month:02d}"
        monthly=[
            t for t in self._transactions if t.date.startswith(month_prefix)
        ]

        income=sum(t.amount for t in monthly if t.type=="income")
        expenses=sum(t.amount for t in monthly if t.type=="expense")
        return {
            "month": month_prefix,
            "income": income,
            "expenses": expenses,
            "balance": income - expenses,
            "transaction_count": len(monthly)
        }
    
    def __str__(self) -> str:
        if not self._transactions:
            return "No transactions recorded yet."

        lines = [
            "=" * 60,
            "FINANCE TRACKER SUMMARY",
            "=" * 60,
            f"Total Income  : ₹{self.total_income:>10.2f}",
            f"Total Expenses: ₹{self.total_expenses:>10.2f}",
            f"Balance       : ₹{self.balance:>10.2f}",
            "=" * 60,
            "TRANSACTIONS",
            "-" * 60,
        ]
        for t in self._transactions:
            lines.append(str(t))
        lines.append("=" * 60)
        return "\n".join(lines)
    
    def view_monthly_summary(tracker: FinanceTracker) -> None:
        try:
            year = int(input("Year (e.g. 2024): "))
            month = int(input("Month (1-12): "))
            summary = tracker.monthly_summary(month, year)
            print(f"\n--- Summary for {summary['month']} ---")
            print(f"Income      : ₹{summary['income']:.2f}")
            print(f"Expenses    : ₹{summary['expenses']:.2f}")
            print(f"Balance     : ₹{summary['balance']:.2f}")
            print(f"Transactions: {summary['transaction_count']}")
        except ValueError:
            print("Please enter valid numbers for year and month.")
