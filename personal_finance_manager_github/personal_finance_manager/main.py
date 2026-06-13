# main.py - Personal Finance Manager Entry Point
# Author: Gaurav Deshmukh
# B.Tech Artificial Intelligence, GHRCEM Pune - 2025
# Description: Main program entry point for the Personal Finance Manager

import sys
import os

# Ensure src/ is importable
sys.path.insert(0, os.path.dirname(__file__))

from src.file_manager import load_expenses, ensure_data_dir
from src.menu import run_menu


def main():
    """Main function - load data and launch menu."""
    ensure_data_dir()
    print("Loading your expense data...")
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} expense(s).")
    run_menu(expenses)


if __name__ == "__main__":
    main()
