# main.py
import database
from datetime import datetime
import reports

def add_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the category (e.g., Food, Entertainment, etc.): ")
    description = input("Enter a description (optional): ")
    date = input("Enter the date (YYYY-MM-DD) or press enter for today's date: ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    database.insert_expense(amount, category, description, date)
    print("Expense added successfully!")

def view_expenses():
    expenses = database.get_expenses()
    print("\n--- Your Expenses ---")
    for expense in expenses:
        print(f"ID: {expense[0]} | Amount: {expense[1]} | Category: {expense[2]} | Description: {expense[3]} | Date: {expense[4]}")

def add_budget():
    category = input("Enter the category for the budget: ")
    budget = float(input("Enter the budget amount: "))
    database.insert_budget(category, budget)
    print(f"Budget for {category} set at {budget}")

def main_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Genereate Monthly Report")
        print("5. Generate Category Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_budget()
        elif choice == "4":
            month = int(input("Enter the month (1-12): "))
            reports.generate_monthly_report(month)
        elif choice == "5":
            reports.generate_category_summary()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    database.create_tables()  # Ensure tables are created
    main_menu()
