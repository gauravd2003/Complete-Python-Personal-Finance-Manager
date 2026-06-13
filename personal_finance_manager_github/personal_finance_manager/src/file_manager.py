# file_manager.py - CSV Read/Write Operations
# Author: Gaurav Deshmukh
# Description: Handles all file I/O for expense data persistence

import csv
import os
import shutil
from datetime import datetime
from src.expense import Expense

DATA_FILE = "data/expenses.csv"
BACKUP_DIR = "data/backups/"
FIELDNAMES = ["date", "category", "amount", "description"]


def ensure_data_dir():
    """Create data directories if they don't exist."""
    os.makedirs("data", exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def load_expenses():
    """
    Load all expenses from CSV file.
    Returns:
        list: List of Expense objects
    """
    ensure_data_dir()
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses
    try:
        with open(DATA_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = Expense(
                        amount=row["amount"],
                        category=row["category"],
                        date=row["date"],
                        description=row["description"]
                    )
                    expenses.append(expense)
                except (KeyError, ValueError):
                    continue  # Skip corrupted rows
    except Exception as e:
        print(f"Error loading expenses: {e}")
    return expenses


def save_expenses(expenses):
    """
    Save all expenses to CSV file.
    Args:
        expenses (list): List of Expense objects
    """
    ensure_data_dir()
    try:
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
        return True
    except Exception as e:
        print(f"Error saving expenses: {e}")
        return False


def backup_data():
    """Create a timestamped backup of expenses data."""
    ensure_data_dir()
    if not os.path.exists(DATA_FILE):
        print("No data file found to backup.")
        return False
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"expenses_backup_{timestamp}.csv")
    try:
        shutil.copy2(DATA_FILE, backup_file)
        print(f"Backup created: {backup_file}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False


def restore_data():
    """Restore from the most recent backup."""
    ensure_data_dir()
    backups = sorted(
        [f for f in os.listdir(BACKUP_DIR) if f.endswith(".csv")],
        reverse=True
    )
    if not backups:
        print("No backup files found.")
        return False
    latest = os.path.join(BACKUP_DIR, backups[0])
    try:
        shutil.copy2(latest, DATA_FILE)
        print(f"Data restored from: {latest}")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False
