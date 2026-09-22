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


def search_by_category(expenses, target_category):
    target_category_lower = target_category.lower()
    matching_expenses = []

    for expense in expenses:
        if expense["category"].lower() == target_category_lower:
            matching_expenses.append(expense)

    return matching_expenses


def total_by_category(expenses, target_category):
    target_category_lower = target_category.lower()
    total = 0

    for expense in expenses:
        if expense["category"].lower() == target_category_lower:
            total += expense["amount"]

    return total


view_expenses(business_expenses)

add_expense(business_expenses, "Website hosting", 200.00, "IT Services")

view_expenses(business_expenses)

print(search_by_category(business_expenses, "FOOD"))
print(total_by_category(business_expenses, "FOOD"))

while True:
    print("\nMenu:")
    print("0. Exit")
    print("1. View all expenses")
    print("2. Add a new expense")
    print("3. Search expenses by category")
    print("4. View total spent in a category")
    choice = input("Choose an option: ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        view_expenses(business_expenses)
    elif choice == "2":
        description = input("Enter expense description: ")
        amount = input("Enter expense amount: ")
        category = input("Enter expense category: ")
        add_expense(business_expenses, description, amount, category)
    elif choice == "3":
        category = input("Enter the category to search for: ")
        matching_expenses = search_by_category(business_expenses, category)
        for expense in matching_expenses:
            print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
    elif choice == "4":
        category = input("Enter the category to total: ")
        total = total_by_category(business_expenses, category)
        print(f"Total spent in {category}: ${total:.2f}")

