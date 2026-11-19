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

# Load Transaction Data
df = pd.read_sql(
    "SELECT * FROM TRANSACTIONS",
    connection
)

connection.close()

# Transaction Type Analysis
type_counts = df["TRANSACTION_TYPE"].value_counts()

print("\n--- TRANSACTION TYPE DISTRIBUTION ---")
print(type_counts)

# Transaction Amount Summary
amount_summary = df.groupby(
    "TRANSACTION_TYPE"
)["AMOUNT"].sum()

print("\n--- TOTAL AMOUNT BY TRANSACTION TYPE ---")
print(amount_summary)

# Channel Analysis
channel_counts = df["CHANNEL"].value_counts()

print("\n--- TRANSACTION CHANNEL DISTRIBUTION ---")
print(channel_counts)

# Overall Statistics
print("\n--- TRANSACTION STATISTICS ---")
print("Total Transactions:", len(df))
print("Total Transaction Amount:", df["AMOUNT"].sum())
print("Average Transaction Amount:", df["AMOUNT"].mean())

# Visualization 1: Transaction Types
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="TRANSACTION_TYPE"
)

plt.title("Transaction Type Distribution")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

# Visualization 2: Transaction Channels
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="CHANNEL",
    order=channel_counts.index
)

plt.title("Transaction Channel Distribution")
plt.xlabel("Channel")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=25)

plt.tight_layout()
plt.show()
