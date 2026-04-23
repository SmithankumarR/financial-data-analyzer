import pandas as pd

# Load data
data = pd.read_csv("transactions.csv")

# Separate income and expense
income = data[data["Type"] == "Income"]
expense = data[data["Type"] == "Expense"]

# Calculate totals
total_income = income["Amount"].sum()
total_expense = expense["Amount"].sum()

print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Net Profit:", total_income - total_expense)