# reports.py - Report Generation Functions
# Author: Gaurav Deshmukh
# Description: Generates expense reports, summaries, and analysis

from collections import defaultdict
from datetime import datetime
import os


def get_total(expenses):
    """Return total of all expenses."""
    return sum(e.amount for e in expenses)


def get_average(expenses):
    """Return average expense amount."""
    if not expenses:
        return 0.0
    return get_total(expenses) / len(expenses)


def get_category_summary(expenses):
    """
    Group expenses by category and calculate totals.
    Returns:
        dict: {category: total_amount}
    """
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return dict(sorted(summary.items(), key=lambda x: x[1], reverse=True))


def get_monthly_summary(expenses):
    """
    Group expenses by month.
    Returns:
        dict: {YYYY-MM: total_amount}
    """
    monthly = defaultdict(float)
    for expense in expenses:
        month = expense.date[:7]  # YYYY-MM
        monthly[month] += expense.amount
    return dict(sorted(monthly.items()))


def search_expenses(expenses, keyword):
    """Search expenses by description or category keyword."""
    keyword = keyword.lower()
    return [e for e in expenses if keyword in e.description.lower() or keyword in e.category.lower()]


def print_category_report(expenses):
    """Print a formatted category-wise expense report."""
    if not expenses:
        print("No expenses to report.")
        return
    summary = get_category_summary(expenses)
    total = get_total(expenses)
    print("\n" + "=" * 55)
    print("         CATEGORY-WISE EXPENSE SUMMARY")
    print("=" * 55)
    print(f"{'Category':<20} {'Amount (Rs.)':<15} {'% of Total':<10}")
    print("-" * 55)
    for category, amount in summary.items():
        pct = (amount / total * 100) if total > 0 else 0
        print(f"{category:<20} Rs.{amount:<12.2f} {pct:.1f}%")
    print("-" * 55)
    print(f"{'TOTAL':<20} Rs.{total:<12.2f} 100.0%")
    print("=" * 55)


def print_monthly_report(expenses):
    """Print a formatted monthly expense report."""
    if not expenses:
        print("No expenses to report.")
        return
    monthly = get_monthly_summary(expenses)
    print("\n" + "=" * 45)
    print("         MONTHLY EXPENSE REPORT")
    print("=" * 45)
    print(f"{'Month':<15} {'Total (Rs.)':<15} {'Expenses'}")
    print("-" * 45)
    for month, total in monthly.items():
        count = sum(1 for e in expenses if e.date[:7] == month)
        print(f"{month:<15} Rs.{total:<12.2f} {count} entries")
    print("-" * 45)
    print(f"Overall Total: Rs.{get_total(expenses):.2f}")
    print(f"Average per Expense: Rs.{get_average(expenses):.2f}")
    print("=" * 45)


def export_report(expenses, filename=None):
    """Export a text summary report to the reports/ folder."""
    os.makedirs("reports", exist_ok=True)
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/expense_report_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write("PERSONAL FINANCE MANAGER - EXPENSE REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total Expenses: Rs.{get_total(expenses):.2f}\n")
        f.write(f"Average Expense: Rs.{get_average(expenses):.2f}\n")
        f.write(f"Number of Entries: {len(expenses)}\n\n")
        f.write("CATEGORY BREAKDOWN:\n")
        for cat, amt in get_category_summary(expenses).items():
            f.write(f"  {cat}: Rs.{amt:.2f}\n")
        f.write("\nALL EXPENSES:\n")
        for e in sorted(expenses, key=lambda x: x.date):
            f.write(f"  {e}\n")
    print(f"Report exported to: {filename}")
