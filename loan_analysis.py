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

# Load Loan Data
df = pd.read_sql(
    "SELECT * FROM LOANS",
    connection
)

connection.close()

# Loan Type Distribution
loan_counts = df["LOAN_TYPE"].value_counts()

print("\n--- LOAN TYPE DISTRIBUTION ---")
print(loan_counts)

# Total Loan Amount by Type
loan_summary = df.groupby(
    "LOAN_TYPE"
)["LOAN_AMOUNT"].sum().sort_values(ascending=False)

print("\n--- TOTAL LOAN AMOUNT BY TYPE ---")
print(loan_summary)

# Loan Statistics
total_loans = len(df)
total_amount = df["LOAN_AMOUNT"].sum()

defaulted_loans = (df["IS_DEFAULTED"] == "Y").sum()
default_rate = (defaulted_loans / total_loans) * 100

print("\n--- LOAN STATISTICS ---")
print("Total Loans:", total_loans)
print("Total Loan Amount:", total_amount)
print("Defaulted Loans:", defaulted_loans)
print("Loan Default Rate:", round(default_rate, 2), "%")

# Chart 1: Loan Type Distribution
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="LOAN_TYPE"
)

plt.title("Loan Type Distribution")
plt.xlabel("Loan Type")
plt.ylabel("Number of Loans")
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

# Chart 2: Default Status
plt.figure(figsize=(7, 7))

default_counts = df["IS_DEFAULTED"].value_counts()

plt.pie(
    default_counts.values,
    labels=["Not Defaulted", "Defaulted"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Loan Default Distribution")

plt.tight_layout()
plt.show()
