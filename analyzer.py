import pandas as pd

# Load data
data = pd.read_csv("transactions.csv")

# Separate income and expense
income = data[data["Type"] == "Income"]
expense = data[data["Type"] == "Expense"]

# Calculate totals
total_income = income["Amount"].sum()
total_expense = expense["Amount"].sum()
net_profit = total_income - total_expense

# Category-wise expense breakdown
category_expense = expense.groupby("Category")["Amount"].sum()

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Monthly summary
monthly_summary = data.groupby(data["Date"].dt.month)["Amount"].sum()

# Tax calculation (simple 10%)
tax = net_profit * 0.10

print("\n==== Monthly Summary ====")
print(monthly_summary)

print("\n==== Tax Estimation ====")
print("Estimated Tax (10%):", tax)

# Output
print("==== Financial Summary ====")
print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Net Profit:", net_profit)

print("\n==== Category-wise Expenses ====")
print(category_expense)