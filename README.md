# Business Expense Tracker

A command-line Python application for managing and analyzing business expenses.

This project was built as part of my Python and AI-assisted development practice. It focuses on working with lists, dictionaries, functions, object-oriented programming, input validation, exception handling, Git, and structured AI prompting.

## Features

- View all business expenses
- Add new expenses
- Search expenses by category
- Calculate total spending by category
- Identify the highest-spending category
- Validate numeric expense amounts
- Handle invalid user input
- Interactive command-line menu

## Project Structure

```text
business-expense-tracker/
│
├── main.py
├── expense_manager.py
├── menu.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

### `main.py`

Acts as the entry point of the application.

It:

- Creates the initial expense data
- Creates an `ExpenseManager` instance
- Creates a `Menu` instance
- Starts the application

### `expense_manager.py`

Contains the `ExpenseManager` class and the business logic of the application.

Current methods include:

- `view_expenses()`
- `add_expense()`
- `search_by_category()`
- `total_by_category()`
- `highest_spending_category()`

### `menu.py`

Contains the `Menu` class responsible for user interaction and navigation through the application.

## Example Data

Expenses are currently represented using a list of dictionaries:

```python
business_expenses = [
    {
        "description": "Store rent",
        "amount": 15000.00,
        "category": "Rent",
    },
    {
        "description": "Supply purchase",
        "amount": 3500.00,
        "category": "Supplies",
    },
]
```

Each dictionary represents one expense and stores its description, amount, and category.

## Input Validation

Expense amounts are received as user input and converted to numbers inside `ExpenseManager`.

If the user enters an invalid amount, the application catches the error and prevents the invalid expense from being added.

Example:

```text
Enter expense amount: expensive
Amount must be a number. Expense not added.
```

## Running the Project

This project uses Python and `uv`.

Clone the repository:

```bash
git clone https://github.com/Anthonymanuelm97/business-expense-tracker.git
```

Enter the project directory:

```bash
cd business-expense-tracker
```

Synchronize the environment:

```bash
uv sync
```

Run the application:

```bash
uv run main.py
```

## Example Menu

```text
Business Expense Tracker

0. Exit
1. View all expenses
2. Add a new expense
3. Search expenses by category
4. View total spent in a category
5. View highest spending category
```

## Concepts Practiced

This project helped reinforce:

- Python variables and data types
- Lists
- Dictionaries
- Lists of dictionaries
- Functions
- `return`
- `for` loops
- Conditional logic
- Classes and objects
- `self`
- Exception handling with `try/except`
- Input validation
- Refactoring
- Separation of responsibilities
- Git commits and version control
- GitHub workflow
- Structured prompting with AI coding assistants

## Development Process

The project was built incrementally.

Instead of generating the entire application at once, each feature was implemented, tested, reviewed with Git, and committed separately.

The development process included:

1. Creating the project environment
2. Adding initial expense data
3. Building basic expense functions
4. Adding category search and totals
5. Building the interactive menu
6. Diagnosing an intentional data-type bug
7. Adding input validation and exception handling
8. Refactoring the application into classes
9. Separating the application into multiple modules

## What I Learned

One of the main lessons from this project was that an error does not always appear where the problem originally started.

For example, an expense amount entered through `input()` was initially stored as a string. The application accepted the value without errors, but the problem appeared later when the program attempted to add that string to numeric expense totals.

This reinforced the importance of validating data when it enters the system.

I also practiced refactoring working code without changing its behavior by separating business logic, user interaction, and application startup into different modules.

## Future Improvements

Possible future improvements include:

- Persistent storage using JSON, CSV, or SQLite
- Delete and edit expense functionality
- Expense IDs
- Date tracking
- Monthly expense reports
- Category summaries
- Automated tests
- Exporting reports to CSV or Excel