
class FinanceError(Exception):
    """Handles all the errors related to financial transactions in your personal finance tracker"""
    pass

class  InvalidAmountError(FinanceError):
    """Raised when the amount entered for transaction is not valid."""
    def __init__(self, amount: float):
        self.amount=amount
        super().__init__(f"Amount must be greater than zero. Got: {amount}")

class InvalidCategoryError(FinanceError):
    """Raised when the category entered is not valid."""
    def __init__(self, category: str):
        self.category=category
        super().__init__(f"Wrong category entered. You entered-{category}")

class TransactionNotFoundError(FinanceError):
    """Raised when a particular transaction can not be found in the records."""
    def __init__(self, transaction_id: str):
        self.transaction_id=transaction_id
        super().__init__(f"Could not find the transaction-{transaction_id}, Enter a valid transaction_id")

class InsufficientFundsError(FinanceError):
    """Raised when the amount entered is greater than the balance present in the account."""
    def __init__(self, amount:float, balance: float):
        self.amount=amount
        self.balance=balance
        super().__init__(f"Cannot process {amount}. "
                        f"Current balance is {balance}. "
                        f"Shortfall: {amount - balance:.2f}")
                
class FileProcessingError(Exception):
    """Raised when a file cannot be read or parsed."""
    def __init__(self, filepath: str, reason: str) -> None:
        self.filepath= filepath
        self.reason= reason
        super().__init__(f"Could not process {filepath}, reason: {reason}")