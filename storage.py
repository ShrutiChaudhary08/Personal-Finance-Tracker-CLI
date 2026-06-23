import json
from tracker import FinanceTracker
from models import Transaction
from exceptions import FileProcessingError

        
def save_data(tracker: FinanceTracker, filepath: str) -> None:
    ls_dicts=[t.to_dict() for t in tracker._transactions]
    try:
        with open(filepath, "w") as f:
            json.dump(ls_dicts, f, indent=4)
    except OSError as e:
        raise FileProcessingError(filepath, "Could not write to file") from e

def load_data(filepath: str) -> list[Transaction]:
    try:
        with open(filepath, "r") as fnew:
            data=json.load(fnew)
            return [Transaction.from_dict(d) for d in data]
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise FileProcessingError(filepath, "File contains invalid JSON") from e



