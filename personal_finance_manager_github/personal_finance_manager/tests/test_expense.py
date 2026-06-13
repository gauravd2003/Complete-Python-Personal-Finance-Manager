# tests/test_expense.py - Unit Tests
# Author: Gaurav Deshmukh

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.expense import Expense
from src.reports import get_total, get_average, get_category_summary
from src.utils import validate_amount, validate_date


def test_expense_creation():
    e = Expense(1500, "Food", "2024-01-15", "Grocery shopping")
    assert e.amount == 1500.0
    assert e.category == "Food"
    assert e.date == "2024-01-15"
    assert e.description == "Grocery shopping"
    print("PASS: test_expense_creation")


def test_invalid_category_defaults_to_other():
    e = Expense(500, "InvalidCat", "2024-01-15", "Test")
    assert e.category == "Other"
    print("PASS: test_invalid_category_defaults_to_other")


def test_expense_to_dict():
    e = Expense(200, "Transport", "2024-02-10", "Bus fare")
    d = e.to_dict()
    assert d["amount"] == 200.0
    assert d["category"] == "Transport"
    print("PASS: test_expense_to_dict")


def test_total_calculation():
    expenses = [
        Expense(100, "Food", "2024-01-01", "Lunch"),
        Expense(200, "Transport", "2024-01-02", "Taxi"),
        Expense(300, "Shopping", "2024-01-03", "Clothes"),
    ]
    assert get_total(expenses) == 600.0
    print("PASS: test_total_calculation")


def test_average_calculation():
    expenses = [
        Expense(100, "Food", "2024-01-01", "Lunch"),
        Expense(300, "Food", "2024-01-02", "Dinner"),
    ]
    assert get_average(expenses) == 200.0
    print("PASS: test_average_calculation")


def test_category_summary():
    expenses = [
        Expense(100, "Food", "2024-01-01", "Lunch"),
        Expense(200, "Food", "2024-01-02", "Dinner"),
        Expense(150, "Transport", "2024-01-03", "Taxi"),
    ]
    summary = get_category_summary(expenses)
    assert summary["Food"] == 300.0
    assert summary["Transport"] == 150.0
    print("PASS: test_category_summary")


def test_validate_amount():
    assert validate_amount("1500") == 1500.0
    assert validate_amount("-100") is None
    assert validate_amount("abc") is None
    print("PASS: test_validate_amount")


def test_validate_date():
    assert validate_date("2024-01-15") == "2024-01-15"
    assert validate_date("15-01-2024") is None
    assert validate_date("not-a-date") is None
    print("PASS: test_validate_date")


if __name__ == "__main__":
    print("\n=== Running Unit Tests ===\n")
    test_expense_creation()
    test_invalid_category_defaults_to_other()
    test_expense_to_dict()
    test_total_calculation()
    test_average_calculation()
    test_category_summary()
    test_validate_amount()
    test_validate_date()
    print("\nAll tests passed!")
