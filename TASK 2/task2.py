import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    try:
        with open('transactions.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {'income': 0, 'expenses': {}}

def save_data(data):
    with open('transactions.json', 'w') as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    save_data(data)
    print("Income added successfully.")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    if category not in data['expenses']:
        data['expenses'][category] = 0
    data['expenses'][category] += amount
    save_data(data)
    print("Expense added successfully.")

def calculate_budget(data):
    total_expenses = sum(data['expenses'].values())
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def analyze_expenses(data):
    print("\nExpense Analysis:")
    for category, amount in data['expenses'].items():
        print(f"{category}: ${amount}")
    print("Total Expenses:", sum(data['expenses'].values()))

def main():
    data = load_data()
    while True:
        clear_screen()
        print("Budget Tracker\n")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            budget = calculate_budget(data)
            print("\nRemaining Budget:", budget)
            input("\nPress Enter to continue...")
        elif choice == '4':
            analyze_expenses(data)
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
