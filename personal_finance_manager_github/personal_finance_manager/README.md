# 💰 Personal Finance Manager

A command-line Python application to track personal expenses, generate reports, and analyze spending patterns — built using Object-Oriented Programming (OOP) principles.

> **Developed by:** Gaurav Deshmukh  
> **Degree:** B.Tech Artificial Intelligence, GHRCEM Pune (2025)  
> **Project Type:** Month 1 Python Programming Mastery Project

---

## 📌 Features

- ✅ Add, view, search, and delete expenses
- ✅ Category-wise expense summary
- ✅ Monthly expense reports
- ✅ Export reports to text files
- ✅ Data backup and restore functionality
- ✅ Input validation and error handling
- ✅ Modular OOP code structure
- ✅ CSV-based data persistence (no external DB needed)

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python 3.8+ | Core language |
| CSV module | Data persistence |
| OOP (Classes) | Expense model |
| Standard Library only | No pip installs needed |

---

## 📁 Project Structure

```
personal_finance_manager/
│
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── src/                    # Source code
│   ├── __init__.py
│   ├── expense.py          # Expense class (OOP model)
│   ├── file_manager.py     # CSV read/write operations
│   ├── menu.py             # Command-line UI
│   ├── reports.py          # Report generation
│   └── utils.py            # Validation & helpers
│
├── data/                   # Data storage
│   ├── expenses.csv        # Main expense data
│   └── backups/            # Auto-generated backups
│
├── reports/                # Exported text reports
├── tests/                  # Unit tests
│   └── test_expense.py
├── docs/                   # Documentation
└── screenshots/            # App screenshots
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher
- No external libraries required

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/gauravdeshmukh/personal-finance-manager.git

# 2. Navigate to project folder
cd personal-finance-manager

# 3. Run the application
python main.py
```

---

## 🚀 How to Use

```
==========================================
       PERSONAL FINANCE MANAGER
==========================================

MAIN MENU:
  1. Add New Expense
  2. View All Expenses
  3. View Category-wise Summary
  4. Generate Monthly Report
  5. Search Expenses
  6. Delete an Expense
  7. Export Report to File
  8. Backup Data
  9. Restore Data
  0. Exit
```

### Adding an Expense
```
--- ADD NEW EXPENSE ---
Enter amount (Rs.): 1500
Categories: Food, Transport, Entertainment, Shopping, Health, Education, Other
Enter category: Food
Enter date (YYYY-MM-DD) [default: 2024-01-15]: 2024-01-15
Enter description: Grocery shopping

Expense added successfully!
  2024-01-15 | Food            |    Rs.1500.00 | Grocery shopping
```

---

## 🧪 Running Tests

```bash
python tests/test_expense.py
```

Expected output:
```
=== Running Unit Tests ===

PASS: test_expense_creation
PASS: test_invalid_category_defaults_to_other
PASS: test_expense_to_dict
PASS: test_total_calculation
PASS: test_average_calculation
PASS: test_category_summary
PASS: test_validate_amount
PASS: test_validate_date

All tests passed!
```

---

## 📊 Sample Report Output

```
=======================================================
         CATEGORY-WISE EXPENSE SUMMARY
=======================================================
Category             Amount (Rs.)    % of Total
-------------------------------------------------------
Food                 Rs.4330.00      36.2%
Shopping             Rs.4300.00      36.0%
Transport            Rs.1100.00       9.2%
Education            Rs.2000.00      16.7%
Health               Rs.950.00        7.9%
-------------------------------------------------------
TOTAL                Rs.11940.00     100.0%
=======================================================
```

---

## 🔑 Key Concepts Demonstrated

- **OOP** — Expense class with attributes, methods, validation
- **File Handling** — CSV read/write using Python's csv module
- **Error Handling** — try/except for all user inputs and file ops
- **Modular Design** — Separate modules for each concern
- **Data Validation** — Amount, date, and category validation
- **Algorithms** — Sorting, filtering, grouping with defaultdict

---

## 👨‍💻 Author

**Gaurav Deshmukh**  
📧 gauravdeshmukh9970@gmail.com  
🔗 GitHub: github.com/gauravdeshmukh  
📍 Nanded, Maharashtra
