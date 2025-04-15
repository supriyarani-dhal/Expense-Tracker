# reports.py
import sqlite3
from tabulate import tabulate
from database import create_connection

def generate_monthly_report(month):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Get all expenses for the given month
    query = f"SELECT * FROM expenses WHERE strftime('%m', date) = '{month:02d}'"
    cursor.execute(query)
    expenses = cursor.fetchall()
    
    if not expenses:
        print(f"No expenses found for month: {month}")
    else:
        print(f"Expenses for month {month}:")
        print(tabulate(expenses, headers=["ID", "Amount", "Category", "Description", "Date"]))
    
    conn.close()

def generate_category_summary():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Get total spending per category
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    categories = cursor.fetchall()
    
    if not categories:
        print("No expenses found!")
    else:
        print("Category-wise spending summary:")
        print(tabulate(categories, headers=["Category", "Total Spending"]))
    
    conn.close()
