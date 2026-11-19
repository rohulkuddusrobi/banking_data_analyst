
import oracledb
import pandas as pd
import os

# Create Reports Folder
os.makedirs("reports", exist_ok=True)

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Data
customers = pd.read_sql("SELECT * FROM CUSTOMERS", connection)
accounts = pd.read_sql("SELECT * FROM ACCOUNTS", connection)
transactions = pd.read_sql("SELECT * FROM TRANSACTIONS", connection)
loans = pd.read_sql("SELECT * FROM LOANS", connection)

connection.close()

# Create Summary Data
summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Total Accounts",
        "Total Transactions",
        "Total Transaction Amount",
        "Total Loan Amount",
        "Defaulted Loans"
    ],
    "Value": [
        len(customers),
        len(accounts),
        len(transactions),
        transactions["AMOUNT"].sum(),
        loans["LOAN_AMOUNT"].sum(),
        (loans["IS_DEFAULTED"] == "Y").sum()
    ]
})

# Export CSV
summary.to_csv(
    "reports/banking_summary.csv",
    index=False
)

# Export Excel with Multiple Sheets
with pd.ExcelWriter(
    "reports/banking_analysis.xlsx",
    engine="openpyxl"
) as writer:

    summary.to_excel(
        writer, sheet_name="Summary", index=False
    )

    customers.to_excel(
        writer, sheet_name="Customers", index=False
    )

    accounts.to_excel(
        writer, sheet_name="Accounts", index=False
    )

    transactions.to_excel(
        writer, sheet_name="Transactions", index=False
    )

    loans.to_excel(
        writer, sheet_name="Loans", index=False
    )

print("CSV and Excel Reports Exported Successfully!")

print("\nFiles Created:")
print("1. reports/banking_summary.csv")
print("2. reports/banking_analysis.xlsx")
