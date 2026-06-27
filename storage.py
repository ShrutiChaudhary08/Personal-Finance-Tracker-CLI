"""Persistence layer for the Personal Finance Tracker.
Provides functions to save and load data using JSON files.
"""
import json
from tracker import FinanceTracker
from models import Transaction
from exceptions import FileProcessingError


def save_data(tracker, filepath: str) -> None:
    """Save all transactions to a JSON file."""
    try:
        data = [t.to_dict() for t in tracker._transactions]
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)   # indent=4 makes the file human-readable
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



