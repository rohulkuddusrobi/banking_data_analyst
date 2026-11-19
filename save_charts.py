
import oracledb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create Charts Folder
os.makedirs("reports/charts", exist_ok=True)

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Data
customers = pd.read_sql("SELECT * FROM CUSTOMERS", connection)
accounts = pd.read_sql("SELECT * FROM ACCOUNTS", connection)
transactions = pd.read_sql(
    "SELECT * FROM TRANSACTIONS WHERE STATUS = 'SUCCESS'",
    connection
)
loans = pd.read_sql("SELECT * FROM LOANS", connection)

connection.close()

sns.set_theme(style="whitegrid")

# 1. Customer by City
plt.figure(figsize=(9, 5))
sns.countplot(data=customers, x="CITY")
plt.title("Customers by City")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("reports/charts/customers_by_city.png", dpi=300)
plt.close()

# 2. Account Type Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=accounts, x="ACCOUNT_TYPE")
plt.title("Account Type Distribution")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("reports/charts/account_type.png", dpi=300)
plt.close()

# 3. Account Balance Distribution
plt.figure(figsize=(8, 5))
sns.histplot(accounts["BALANCE"], bins=8, kde=True)
plt.title("Account Balance Distribution")
plt.tight_layout()
plt.savefig("reports/charts/account_balance.png", dpi=300)
plt.close()

# 4. Transaction Type Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=transactions, x="TRANSACTION_TYPE")
plt.title("Transaction Type Distribution")
plt.tight_layout()
plt.savefig("reports/charts/transaction_type.png", dpi=300)
plt.close()

# 5. Transaction Channel Distribution
plt.figure(figsize=(9, 5))
sns.countplot(data=transactions, x="CHANNEL")
plt.title("Transaction Channel Distribution")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("reports/charts/transaction_channel.png", dpi=300)
plt.close()

# 6. Loan Status Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=loans, x="LOAN_STATUS")
plt.title("Loan Status Distribution")
plt.tight_layout()
plt.savefig("reports/charts/loan_status.png", dpi=300)
plt.close()

# 7. Loan Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(loans["LOAN_AMOUNT"], bins=8, kde=True)
plt.title("Loan Amount Distribution")
plt.tight_layout()
plt.savefig("reports/charts/loan_amount.png", dpi=300)
plt.close()

print("All 7 Charts Saved Successfully!")
print("Location: reports/charts/")
