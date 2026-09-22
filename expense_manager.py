class ExpenseManager:
    def __init__(self, expenses):
        self.expenses = expenses

    def view_expenses(self):
        for expense in self.expenses:
            print(
                f"Description: {expense['description']}, "
                f"Amount: ${expense['amount']:.2f}, "
                f"Category: {expense['category']}"
            )

    def add_expense(self, description, amount, category):
        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a number. Expense not added.")
            return None

        new_expense = {
            "description": description,
            "amount": amount,
            "category": category,
        }

        self.expenses.append(new_expense)
        return new_expense

    def search_by_category(self, target_category):
        matching_expenses = []

        for expense in self.expenses:
            if expense["category"].lower() == target_category.lower():
                matching_expenses.append(expense)

        return matching_expenses

    def total_by_category(self, target_category):
        total = 0

        for expense in self.expenses:
            if expense["category"].lower() == target_category.lower():
                total += expense["amount"]

        return total

    def highest_spending_category(self):
        totals = {}

        for expense in self.expenses:
            category = expense["category"]
            totals[category] = totals.get(category, 0) + expense["amount"]

        return max(totals, key=totals.get)
