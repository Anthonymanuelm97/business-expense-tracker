business_expenses = [
    {"description": "Store rent", "amount": 15000.00, "category": "Rent"},
    {"description": "Supply purchase", "amount": 3500.00, "category": "Supplies"},
    {"description": "Social media advertising",
        "amount": 1200.00, "category": "Marketing"},
]

def add_expense(expenses, description, amount, category):
    new_expense = {"description": description, "amount": amount, "category": category}
    expenses.append(new_expense)
    return new_expense

def view_expenses(expenses):
    for expense in expenses:
        print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}")


view_expenses(business_expenses)

add_expense(business_expenses, "Website hosting", 200.00, "IT Services")

view_expenses(business_expenses)