# expense.py - Expense class definition
# Author: Gaurav Deshmukh
# Description: Defines the Expense data model with OOP principles

from datetime import datetime


class Expense:
    """
    Represents a single expense entry.
    Attributes:
        amount (float): The expense amount in INR
        category (str): Category of expense (Food, Transport, etc.)
        date (str): Date of expense in YYYY-MM-DD format
        description (str): Brief description of the expense
    """

    VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Health", "Education", "Other"]

    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = self._validate_category(category)
        self.date = self._validate_date(date)
        self.description = description.strip()

    def _validate_category(self, category):
        """Validate and return category, default to 'Other' if invalid."""
        if category in self.VALID_CATEGORIES:
            return category
        return "Other"

    def _validate_date(self, date):
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            return datetime.today().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert expense to dictionary for CSV storage."""
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

    def __str__(self):
        return f"{self.date} | {self.category:<15} | Rs.{self.amount:>10.2f} | {self.description}"

    def __repr__(self):
        return f"Expense(amount={self.amount}, category='{self.category}', date='{self.date}')"
