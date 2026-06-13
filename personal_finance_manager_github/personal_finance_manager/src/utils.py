# utils.py - Utility Functions and Validation
# Author: Gaurav Deshmukh
# Description: Input validation and formatting helper functions

from datetime import datetime
from src.expense import Expense


def validate_amount(value):
    """
    Validate that input is a positive number.
    Returns:
        float or None
    """
    try:
        amount = float(value)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None


def validate_date(date_str):
    """
    Validate date in YYYY-MM-DD format.
    Returns:
        str or None
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD (e.g., 2024-01-15).")
        return None


def get_valid_input(prompt, validator=None, default=None):
    """
    Prompt user for input with optional validation.
    Args:
        prompt (str): Display message
        validator (callable): Optional validation function
        default: Default value if user presses Enter
    Returns:
        Validated user input
    """
    while True:
        value = input(prompt).strip()
        if not value and default is not None:
            return default
        if validator:
            result = validator(value)
            if result is not None:
                return result
        elif value:
            return value
        else:
            print("Input cannot be empty.")


def format_currency(amount):
    """Format amount as Indian Rupees string."""
    return f"Rs.{amount:,.2f}"


def print_divider(char="=", length=50):
    """Print a divider line."""
    print(char * length)


def today_date():
    """Return today's date as YYYY-MM-DD string."""
    return datetime.today().strftime("%Y-%m-%d")


def display_expenses_table(expenses):
    """Display expenses in a formatted table."""
    if not expenses:
        print("No expenses found.")
        return
    print("\n" + "=" * 70)
    print(f"{'#':<4} {'Date':<12} {'Category':<15} {'Amount':>12}  {'Description'}")
    print("-" * 70)
    for i, e in enumerate(expenses, 1):
        desc = e.description[:25] + "..." if len(e.description) > 25 else e.description
        print(f"{i:<4} {e.date:<12} {e.category:<15} Rs.{e.amount:>9.2f}  {desc}")
    print("=" * 70)
    print(f"Total: {format_currency(sum(e.amount for e in expenses))} ({len(expenses)} entries)")
