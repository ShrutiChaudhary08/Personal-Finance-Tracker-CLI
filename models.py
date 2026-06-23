from exceptions import InvalidAmountError,  InvalidCategoryError,TransactionNotFoundError, InsufficientFundsError

Valid_Categories = [
    "salary", "food", "rent", "transport",
    "entertainment", "health", "savings", "other"
]

Valid_Types = ["income", "expense"]

class Transaction:
    """Represents a single financial transaction"""
    def __init__(self, 
                 transaction_id: str,
                 transaction_type: str,
                 amount: float, 
                 category: str, 
                 date: str , 
                 description: str
                 ) -> None:
        self.transaction_id=transaction_id
        self.type=transaction_type # Income or Expense
        self.amount=amount
        self.category=category
        self.date=date
        self.description=description
    
    #----------------Amount property------------------

    @property #This is getter
    def amount(self) -> float:
        return self._amount
    
    @amount.setter
    def amount(self, value: float) -> None:
        if value<=0:
            raise InvalidAmountError(value)
        self._amount=value  

     #----------------Type property------------------

    @property
    def type(self) -> str:
        return self._type      
    
    @type.setter
    def type(self, type: str) -> None:
        if type.lower() not in Valid_Types:
            raise InvalidCategoryError(type)
        self._type=type.lower()

     #----------------Category property------------------

    @property
    def category(self) -> str:
        return self._category      
    
    @category.setter
    def category(self, value: str) -> None:
        if value.lower() not in Valid_Categories:
            raise InvalidCategoryError(type)
        self._category=value.lower()


    #Conversion of a transaction into a plain dictionary for json file.

    def to_dict(self) -> dict:
        """Converting a transaction to a plain dict"""
        return{
            "transaction_id": self.transaction_id,
            "type": self._type,
            "amount": self._amount,
            "category": self._category,
            "date": self.date,
            "description": self.description
        }
        

    @classmethod
    def from_dict(cls, data: dict) ->"Transaction":
        return cls(
            transaction_id=data["transaction_id"],
            transaction_type=data["type"], #Since cls stands for the class itself which here is transaction therefore, it returns "Transaction"
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"]
        )

     #----------------Display------------------


    def __str__(self) -> str:
         sign = "+" if self._type == "income" else "-"
         return (
            f"[{self.transaction_id}] {self.date} | "
            f"{self._type.upper():8} | "
            f"{sign}₹{self._amount:>10.2f} | "
            f"{self._category:15} | {self.description}"
        )

    def __repr__(self):
        def __repr__(self) -> str:
            return (
            f"Transaction(id={self.transaction_id!r}, "
            f"type={self._type!r}, amount={self._amount}, "
            f"category={self._category!r}, date={self.date!r})"
        )