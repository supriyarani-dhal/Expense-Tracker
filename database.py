# database.py
import sqlite3

def create_connection():
    conn = sqlite3.connect("expenses.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create expenses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL)''')
    
    # Create budget table
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT NOT NULL,
                        budget REAL NOT NULL)''')
    
    conn.commit()
    conn.close()

def insert_expense(amount, category, description, date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))
    conn.commit()
    conn.close()

def insert_budget(category, budget):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO budget (category, budget) VALUES (?, ?)", (category, budget))
    conn.commit()
    conn.close()

def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def get_budget():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budget")
    budget = cursor.fetchall()
    conn.close()
    return budget
