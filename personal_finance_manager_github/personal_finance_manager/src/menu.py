# menu.py - Command-Line Interface
# Author: Gaurav Deshmukh
# Description: Interactive menu system for the Personal Finance Manager

from src.expense import Expense
from src.file_manager import save_expenses, backup_data, restore_data
from src.reports import (
    print_category_report, print_monthly_report, export_report, search_expenses
)
from src.utils import (
    validate_amount, validate_date, get_valid_input,
    display_expenses_table, today_date, print_divider
)


def print_banner():
    """Display application banner."""
    print("\n" + "=" * 50)
    print("       PERSONAL FINANCE MANAGER")
    print("       Developed by: Gaurav Deshmukh")
    print("=" * 50)


def print_main_menu():
    """Display main menu options."""
    print("\nMAIN MENU:")
    print("  1. Add New Expense")
    print("  2. View All Expenses")
    print("  3. View Category-wise Summary")
    print("  4. Generate Monthly Report")
    print("  5. Search Expenses")
    print("  6. Delete an Expense")
    print("  7. Export Report to File")
    print("  8. Backup Data")
    print("  9. Restore Data")
    print("  0. Exit")
    print_divider("-", 50)


def add_expense(expenses):
    """Handle adding a new expense."""
    print("\n--- ADD NEW EXPENSE ---")
    amount = get_valid_input("Enter amount (Rs.): ", validate_amount)
    print(f"Categories: {', '.join(Expense.VALID_CATEGORIES)}")
    category = get_valid_input("Enter category: ", default="Other")
    if category not in Expense.VALID_CATEGORIES:
        category = "Other"
    date = get_valid_input(
        f"Enter date (YYYY-MM-DD) [default: {today_date()}]: ",
        validate_date,
        default=today_date()
    )
    description = get_valid_input("Enter description: ")
    expense = Expense(amount, category, date, description)
    expenses.append(expense)
    if save_expenses(expenses):
        print(f"\nExpense added successfully!")
        print(f"  {expense}")
    else:
        print("Error saving expense.")
    input("\nPress Enter to continue...")


def view_all_expenses(expenses):
    """Display all expenses in a table."""
    print("\n--- ALL EXPENSES ---")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        display_expenses_table(sorted(expenses, key=lambda x: x.date))
    input("\nPress Enter to continue...")


def delete_expense(expenses):
    """Handle deleting an expense."""
    print("\n--- DELETE EXPENSE ---")
    display_expenses_table(expenses)
    if not expenses:
        input("\nPress Enter to continue...")
        return
    try:
        idx = int(input("\nEnter expense number to delete (0 to cancel): "))
        if idx == 0:
            return
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")
    input("\nPress Enter to continue...")


def search_menu(expenses):
    """Handle expense search."""
    print("\n--- SEARCH EXPENSES ---")
    keyword = input("Enter search keyword (category or description): ").strip()
    results = search_expenses(expenses, keyword)
    if results:
        print(f"\nFound {len(results)} matching expense(s):")
        display_expenses_table(results)
    else:
        print(f"No expenses found matching '{keyword}'.")
    input("\nPress Enter to continue...")


def run_menu(expenses):
    """Main menu loop."""
    print_banner()
    while True:
        print_main_menu()
        choice = input("Enter your choice (0-9): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            print_category_report(expenses)
            input("\nPress Enter to continue...")
        elif choice == "4":
            print_monthly_report(expenses)
            input("\nPress Enter to continue...")
        elif choice == "5":
            search_menu(expenses)
        elif choice == "6":
            delete_expense(expenses)
        elif choice == "7":
            export_report(expenses)
            input("\nPress Enter to continue...")
        elif choice == "8":
            backup_data()
            input("\nPress Enter to continue...")
        elif choice == "9":
            restore_data()
            expenses.clear()
            from src.file_manager import load_expenses
            expenses.extend(load_expenses())
            input("\nPress Enter to continue...")
        elif choice == "0":
            print("\nThank you for using Personal Finance Manager!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 0-9.")
