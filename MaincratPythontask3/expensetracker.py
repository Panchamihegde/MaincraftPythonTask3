import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Ensure CSV exists with headers
def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])

# Add new expense
def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc.): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])

    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n--- All Expenses ---")
        for row in reader:
            print(row)

# Search expenses by category
def search_by_category():
    category = input("Enter category to search: ")
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print(f"\n--- Expenses in category: {category} ---")
        found = False
        for row in reader:
            if row["Category"].lower() == category.lower():
                print(row)
                found = True
        if not found:
            print("No expenses found in this category.")

# Calculate total per category
def total_per_category():
    category_totals = {}
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            category_totals[category] = category_totals.get(category, 0) + amount

    print("\n--- Total Spending by Category ---")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")

# Calculate monthly spending
def monthly_spending():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])
    print(f"\nTotal spending in {month}: ₹{total:.2f}")

# Main Menu
def main():
    initialize_csv()
    while True:
        print("\n--- Expense Tracker 2.0 ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Total Spending per Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_per_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
