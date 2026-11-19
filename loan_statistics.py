import os

import oracledb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

df = pd.read_sql("SELECT * FROM LOANS", connection)
connection.close()

# Loan Amount Statistics
loan_amount = df["LOAN_AMOUNT"]

print("\n--- LOAN STATISTICS ---")
print("Total Loans:", len(df))
print("Total Loan Amount:", loan_amount.sum())
print("Mean:", loan_amount.mean())
print("Median:", loan_amount.median())
print("Standard Deviation:", loan_amount.std())
print("Minimum:", loan_amount.min())
print("Maximum:", loan_amount.max())

# Default Analysis
default_count = (df["IS_DEFAULTED"] == "Y").sum()
default_rate = (default_count / len(df)) * 100

print("\n--- LOAN DEFAULT ANALYSIS ---")
print("Defaulted Loans:", default_count)
print("Default Rate:", round(default_rate, 2), "%")

# Loan Amount Distribution
plt.figure(figsize=(9, 5))

sns.histplot(
    loan_amount,
    bins=8,
    kde=True
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount (BDT)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Loan Status Distribution
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="LOAN_STATUS"
)

plt.title("Loan Status Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Loans")
plt.tight_layout()
plt.show()
