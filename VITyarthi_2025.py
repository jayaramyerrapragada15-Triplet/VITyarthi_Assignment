import sqlite3
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

# Create table if not exists
cur.execute("""
Create table if not exists expenses (
    date TEXT,
    category TEXT,
    amount REAL
)
""")
conn.commit()

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter the category of expenditure (Food/Travel/Study/Other): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    cur.execute("Insert into  expenses values (?, ?, ?)", (date, category, amount))
    conn.commit()
    print("Expense added!")

def view_expenses():
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    print("\n--- All Expenses ---")
    for row in rows:
        print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}")

def generate_report():
    cur.execute("SELECT amount, category FROM expenses")
    rows = cur.fetchall()

    total = sum(r[0] for r in rows)
    category_totals = {}

    for amount, category in rows:
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n--- Expense Report ---")
    print(f"Your Total Expenses: ₹{total}")
    for c, amt in category_totals.items():
        percent = (amt / total) * 100 if total > 0 else 0
        print(f"{c}: ₹{amt} ({percent:.2f}%)")

    # Pie chart of added expenses
    if category_totals:
        plt.figure(figsize=(6,6))
        plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
        plt.title("Expense Distribution by Category")
        plt.savefig("chart.png")
        plt.close()
        print("Pie chart saved as 'chart.png'. Open it to view.")


def search_expenses():
    key = input("Search by date or category: ")
    cur.execute("SELECT * FROM expenses WHERE date LIKE ? OR category LIKE ?", (f"%{key}%", f"%{key}%"))
    rows = cur.fetchall()


    if rows:
        print(f"\n--- Search Results for '{key}' ---")
        for r in rows:
            print(f"Date: {r[0]}, Category: {r[1]}, Amount: ₹{r[2]}")
    else:
        print("Result not found.")


def reset_data():
    confirm = input("Are you sure you want to delete ALL expenses? (y/n): ")
    if confirm.lower() == "y":
        cur.execute("DELETE FROM expenses")
        conn.commit()
        print("All expenses cleared!")
    else:
        print("Reset cancelled.")

def main_menu():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Report (with Pie Chart)")
        print("4. Search Expenses")
        print("5. Exit")
        print("6. Reset all Data")

        choice = input("Enter choice: ")
        if choice == "1": add_expense()
        elif choice == "2": view_expenses()
        elif choice == "3": generate_report()
        elif choice == "4": search_expenses()
        elif choice  == "5":
            confirm = input("Do you want to delete all expenses before exiting? (y/n): ")
            if confirm.lower() == "y":
                cur.execute("DELETE FROM expenses")
                conn.commit()
                print("All expenses deleted.")
            conn.close()
            print("Good Work. Goodbye!")
            break
        elif choice == "6": reset_data()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()