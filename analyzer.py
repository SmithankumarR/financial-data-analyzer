# import pandas as pd

# # Load data
# data = pd.read_csv("transactions.csv")

# # Separate income and expense
# income = data[data["Type"] == "Income"]
# expense = data[data["Type"] == "Expense"]

# # Calculate totals
# total_income = income["Amount"].sum()
# total_expense = expense["Amount"].sum()
# net_profit = total_income - total_expense

# # Category-wise expense breakdown
# category_expense = expense.groupby("Category")["Amount"].sum()

# # Convert Date column to datetime
# data["Date"] = pd.to_datetime(data["Date"])

# # Monthly summary
# monthly_summary = data.groupby(data["Date"].dt.month)["Amount"].sum()

# # Tax calculation (simple 10%)
# tax = net_profit * 0.10

# # Output
# print("==== Financial Summary ====")
# print("Total Income:", total_income)
# print("Total Expense:", total_expense)
# print("Net Profit:", net_profit)

# print("\n==== Category-wise Expenses ====")
# print(category_expense)

# print("\n==== Monthly Summary ====")
# print(monthly_summary)

# print("\n==== Tax Estimation ====")
# print("Estimated Tax (10%):", tax)


########### code optimised ###########
import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data["Date"] = pd.to_datetime(data["Date"])
        return data
    except Exception as e:
        print("Error loading file:", e)
        return None


def calculate_summary(data):
    income = data[data["Type"] == "Income"]
    expenses = data[data["Type"] == "Expense"]

    total_income = income["Amount"].sum()
    total_expense = expenses["Amount"].sum()
    net_profit = total_income - total_expense

    return total_income, total_expense, net_profit, expenses


def category_breakdown(expenses):
    return expenses.groupby("Category")["Amount"].sum().sort_values(ascending=False)


def monthly_summary(data):
    return data.groupby(data["Date"].dt.to_period("M"))["Amount"].sum()


def tax_estimation(net_profit):
    tax_rate = 0.10  # 10% tax
    return net_profit * tax_rate


def main():
    file_path = "transactions.csv"

    # Load data
    data = load_data(file_path)
    if data is None:
        return

    # Calculate summary
    total_income, total_expense, net_profit, expenses = calculate_summary(data)

    # Display results
    print("==== Financial Summary ====")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Net Profit: ₹{net_profit}")

    print("\n==== Category-wise Expenses ====")
    print(category_breakdown(expenses))

    print("\n==== Monthly Summary ====")
    print(monthly_summary(data))

    print("\n==== Tax Estimation ====")
    print(f"Estimated Tax (10%): ₹{tax_estimation(net_profit)}")


if __name__ == "__main__":
    main()