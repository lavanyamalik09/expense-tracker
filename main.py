import sqlite3

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )

    conn.commit()
    conn.close()

    print("Expense added successfully!")

def view_expenses():
    import sqlite3
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\nAll Expenses:")

    total = 0

    for row in rows:
        print(row)
        total += row[1]

    print("\nTotal Expense:", total)

    conn.close()

def filter_by_category():
    import sqlite3

    category = input("Enter category to filter: ")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()

    print("\nFiltered Expenses:")

    total = 0

    for row in rows:
        print(row)
        total += row[1]

    print("\nTotal for", category, ":", total)

    conn.close()

def export_to_csv():
    import sqlite3
    import csv

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Amount", "Category", "Date"])  # header
        writer.writerows(rows)

    conn.close()

    print("Data exported to expenses.csv successfully!")

def monthly_report():
    import sqlite3

    month = input("Enter month (YYYY-MM): ")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE date LIKE ?",
        (month + "%",)
    )

    rows = cursor.fetchall()

    print("\nMonthly Report:")

    total = 0

    for row in rows:
        print(row)
        total += row[1]

    print("\nTotal for", month, ":", total)

    conn.close()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Export to CSV")
    print("5. Monthly Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_by_category()                

    elif choice == "4":
        export_to_csv()

    elif choice == "5":
        monthly_report()
    
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")

