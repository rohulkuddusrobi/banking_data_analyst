import os

import oracledb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Account Data
accounts = pd.read_sql(
    "SELECT ACCOUNT_ID, BALANCE FROM ACCOUNTS",
    connection
)

# Load Transaction Data
transactions = pd.read_sql(
    "SELECT ACCOUNT_ID, AMOUNT FROM TRANSACTIONS",
    connection
)

connection.close()

# Aggregate transaction amount by account
transaction_summary = transactions.groupby(
    "ACCOUNT_ID"
)["AMOUNT"].sum().reset_index()

transaction_summary.rename(
    columns={"AMOUNT": "TOTAL_TRANSACTION_AMOUNT"},
    inplace=True
)

# Merge Account and Transaction Data
df = pd.merge(
    accounts,
    transaction_summary,
    on="ACCOUNT_ID",
    how="inner"
)

# Correlation
correlation = df[
    ["BALANCE", "TOTAL_TRANSACTION_AMOUNT"]
].corr()

print("\n--- CORRELATION MATRIX ---")
print(correlation)

# Heatmap
plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Account Balance vs Transaction Amount")
plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="BALANCE",
    y="TOTAL_TRANSACTION_AMOUNT"
)

plt.title("Account Balance vs Transaction Amount")
plt.xlabel("Account Balance (BDT)")
plt.ylabel("Total Transaction Amount (BDT)")

plt.tight_layout()
plt.show()
