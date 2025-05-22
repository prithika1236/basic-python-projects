class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expenses:")
        for expense in self.expenses:
            print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
