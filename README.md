# Expense Tracker

A simple CLI-based **Expense Tracker** that stores expenses in an SQLite database (`expenses.db`).  
Built with Python and Matplotlib, this tool lets users add/view/search expenses, generate a category-wise expense report, and save a pie chart visualization.

---

## Project Overview

This lightweight project allows users to record expenses (date, category, amount), view all entries, search by date or category, generate a summary report with category percentages, and export a pie chart (`chart.png`) illustrating expense distribution.

---

## Features

- Add an expense (date, category, amount)
- View all recorded expenses
- Search expenses by date or category (SQL `LIKE`)
- Generate a summary report with per-category totals and percentages
- Save a pie chart visualization (`chart.png`)
- Reset / delete all stored expenses

---

## Technologies / Tools

- Python 3.8+
- SQLite (`sqlite3` — built-in)
- Matplotlib (for chart generation)
- Standard library modules (`typing` — optional)

---

# Installation

1. Install Python (3.8 or newer recommended).  
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
1. Install Python (3.8 or newer recommended).  
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
