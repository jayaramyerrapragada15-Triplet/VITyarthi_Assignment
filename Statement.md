# Problem Statement — Expense Tracker

## 1. Introduction
The Expense Tracker is a Python‑based system designed to help users record, manage, and analyze their daily expenditures.  
It uses SQLite for persistent data storage and supports visualization through charts.  
This aligns with the style and structure of the sample project report provided in the reference document.

## 2. Problem Statement
Users often struggle to maintain a structured record of expenses, leading to poor financial planning.  
Manual tracking is time‑consuming, inefficient, and prone to data loss.

### Challenges
- No centralized location for storing expenses  
- Difficulty identifying major spending categories  
- Lack of visual overview of spending habits  
- No quick search/filtering for past entries  

## 3. Functional Requirements
| ID | Requirement | Description |
|----|-------------|-------------|
| FR1 | Add Expense | System must allow adding a date, category, and amount |
| FR2 | View Expenses | Display all expenses stored in the database |
| FR3 | Search | Allow searching by category or date |
| FR4 | Expense Report | Compute totals and generate category‑wise breakdown |
| FR5 | Visualization | Produce a pie chart of category spending |
| FR6 | Reset | Option to clear all stored expenses |
| FR7 | Persistent Storage | Use SQLite database |

## 4. Non‑functional Requirements
### Performance
- Fast insertion and retrieval  
- Pie chart generation within seconds  

### Reliability
- Data stored in persistent database  
- Proper error handling  

### Usability
- Simple CLI menu  
- Clear instructions & outputs  

### Maintainability
- Modular code  
- Easy to extend categories or add new features  

## 5. System Architecture
- SQLite database  
- Python script handling CRUD operations  
- Matplotlib for chart generation  
(No diagrams required)

## 6. Implementation Summary
The implementation includes:
- SQLite table creation  
- Add, view, search, reset operations  
- Report generation with charts  
- Menu‑based interface  

## 7. Results
The system successfully:
- Stores and retrieves expenses  
- Generates pie‑chart‑based reports  
- Provides meaningful analytics  

## 8. Challenges Faced
- Input validation (amount, date formats)  
- Ensuring data consistency  
- Handling empty datasets during reporting  

## 9. Future Enhancements
- GUI support  
- Export to CSV/PDF  
- Cloud‑synced storage  
- Mobile app version  

## 10. Conclusion
The Expense Tracker is a functional and reliable tool for everyday financial management.  
It offers simple interaction, persistent storage, and visual financial insights.  
