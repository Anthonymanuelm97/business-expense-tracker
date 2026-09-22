from expense_manager import ExpenseManager
from menu import Menu


def main():
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
        {
            "description": "Social media advertising",
            "amount": 1200.00,
            "category": "Marketing",
        },
    ]

    manager = ExpenseManager(business_expenses)
    menu = Menu(manager)
    menu.run()


if __name__ == "__main__":
    main()