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
df = pd.read_sql("""
    SELECT TRANSACTION_DATE, AMOUNT, TRANSACTION_TYPE
    FROM TRANSACTIONS
    WHERE STATUS = 'SUCCESS'
""", connection)

connection.close()

# Convert date
df["TRANSACTION_DATE"] = pd.to_datetime(
    df["TRANSACTION_DATE"]
)

# Extract date only
df["DATE"] = df["TRANSACTION_DATE"].dt.date

# Daily Analysis
daily_summary = df.groupby("DATE").agg(
    TOTAL_TRANSACTIONS=("AMOUNT", "count"),
    TOTAL_AMOUNT=("AMOUNT", "sum"),
    AVERAGE_AMOUNT=("AMOUNT", "mean")
).reset_index()

print("\n--- DAILY TRANSACTION SUMMARY ---")
print(daily_summary.to_string(index=False))

# Daily Transaction Amount Chart
plt.figure(figsize=(10, 5))

sns.lineplot(
    data=daily_summary,
    x="DATE",
    y="TOTAL_AMOUNT",
    marker="o"
)

plt.title("Daily Transaction Amount Trend")
plt.xlabel("Date")
plt.ylabel("Transaction Amount (BDT)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Daily Transaction Count Chart
plt.figure(figsize=(10, 5))

sns.barplot(
    data=daily_summary,
    x="DATE",
    y="TOTAL_TRANSACTIONS"
)

plt.title("Daily Transaction Count")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
