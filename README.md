# Personal-Finance-Tracker-CLI

A command-line personal finance tracker built in Python.

-->> Features
- Add income and expense transactions
- Real-time balance calculation
- Filter transactions by category
- Monthly spending summaries
- Remove transactions by ID
- Persistent storage with JSON
- Full input validation with custom exceptions

-->> Project Structure
finance_tracker/
├── exceptions.py   — Custom exception hierarchy
├── models.py       — Transaction class with validation
├── tracker.py      — Core business logic
├── storage.py      — JSON save and load
└── main.py         — CLI interface

-->> How to run
python main.py

-->> How to test
python test_project.py

--->> Tech used
- Pure Python — OOP architecture
- Custom exception hierarchy  
- @property for computed values and validation
- JSON for persistent storage
- No external dependencies