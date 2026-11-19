import os

import oracledb
import pandas as pd

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Data
customers = pd.read_sql(
    "SELECT * FROM CUSTOMERS", connection
)

accounts = pd.read_sql(
    "SELECT * FROM ACCOUNTS", connection
)

transactions = pd.read_sql(
    "SELECT * FROM TRANSACTIONS WHERE STATUS = 'SUCCESS'",
    connection
)

loans = pd.read_sql(
    "SELECT * FROM LOANS", connection
)

connection.close()

print("\n========== BANKING BUSINESS INSIGHTS ==========")

# 1. Customer Insights
print("\n1. CUSTOMER INSIGHTS")
print("Total Customers:", len(customers))
print("Active Customers:", (customers["STATUS"] == "ACTIVE").sum())

# 2. Account Insights
print("\n2. ACCOUNT INSIGHTS")
print("Total Accounts:", len(accounts))
print("Total Deposits:", accounts["BALANCE"].sum())
print("Average Account Balance:", round(accounts["BALANCE"].mean(), 2))

# 3. Transaction Insights
print("\n3. TRANSACTION INSIGHTS")
print("Total Transactions:", len(transactions))
print("Total Transaction Amount:", transactions["AMOUNT"].sum())
print("Average Transaction:", round(transactions["AMOUNT"].mean(), 2))

# 4. Loan Insights
print("\n4. LOAN INSIGHTS")
print("Total Loans:", len(loans))
print("Total Loan Amount:", loans["LOAN_AMOUNT"].sum())

default_count = (loans["IS_DEFAULTED"] == "Y").sum()
default_rate = default_count / len(loans) * 100

print("Defaulted Loans:", default_count)
print("Loan Default Rate:", round(default_rate, 2), "%")

# 5. Account Type Insights
print("\n5. ACCOUNT TYPE INSIGHTS")

account_summary = accounts.groupby("ACCOUNT_TYPE").agg(
    TOTAL_ACCOUNTS=("ACCOUNT_ID", "count"),
    TOTAL_BALANCE=("BALANCE", "sum")
)

print(account_summary)

print("\n========== INSIGHT REPORT COMPLETED ==========")
