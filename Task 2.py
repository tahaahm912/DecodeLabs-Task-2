import json
import os

FILE_NAME = "expenses.json"

MONTHS = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
]


# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# Show month menu
def choose_month():
    print("\nSelect Month:")
    for i, m in enumerate(MONTHS, start=1):
        print(i, "->", m.capitalize())

    choice = int(input("Enter month number: "))

    if 1 <= choice <= 12:
        return MONTHS[choice - 1]
    else:
        print("Invalid choice, defaulting to Jan")
        return "jan"


# Add expense
def add_expense():
    data = load_data()

    month = choose_month()
    amount = float(input("Enter expense amount: "))

    if month in data:
        data[month].append(amount)
    else:
        data[month] = [amount]

    save_data(data)
    print("Expense added successfully!\n")


# View monthly expense
def view_month():
    data = load_data()

    month = choose_month()

    if month in data and data[month]:
        print(f"\nExpenses for {month.capitalize()}: {data[month]}")
        print("Total:", sum(data[month]), "\n")
    else:
        print("No expenses found for this month.\n")


# Show all data
def show_all():
    data = load_data()

    if not data:
        print("No expenses recorded yet.\n")
        return

    grand_total = 0

    print("\n===== All Expenses =====")
    for month in MONTHS:
        if month in data:
            total = sum(data[month])
            grand_total += total
            print(month.capitalize(), "->", data[month], "| Total:", total)

    print("\nOverall Total Spent:", grand_total, "\n")


# Menu system
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Month Expense")
    print("3. Show All Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_month()
    elif choice == "3":
        show_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice!\n")