class Menu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\nBusiness Expense Tracker")
            print("0. Exit")
            print("1. View all expenses")
            print("2. Add a new expense")
            print("3. Search expenses by category")
            print("4. View total spent in a category")
            print("5. View highest spending category")

            choice = input("Choose an option: ")

            if choice == "0":
                print("Goodbye!")
                break

            elif choice == "1":
                self.manager.view_expenses()

            elif choice == "2":
                description = input("Enter expense description: ")
                amount = input("Enter expense amount: ")
                category = input("Enter expense category: ")

                expense = self.manager.add_expense(description, amount, category)

                if expense is not None:
                    print("Expense added successfully.")

            elif choice == "3":
                category = input("Enter the category to search: ")
                results = self.manager.search_by_category(category)

                for expense in results:
                    print(
                        f"{expense['description']}: "
                        f"${expense['amount']:.2f}"
                    )

            elif choice == "4":
                category = input("Enter the category to total: ")
                total = self.manager.total_by_category(category)

                print(f"Total spent in {category}: ${total:.2f}")

            elif choice == "5":
                category = self.manager.highest_spending_category()
                print(f"Highest spending category: {category}")

            else:
                print("Invalid option.")
