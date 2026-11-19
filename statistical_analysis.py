import os

import oracledb
import pandas as pd

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Account Data
df = pd.read_sql(
    "SELECT * FROM ACCOUNTS",
    connection
)

connection.close()

# Statistical Analysis
balance = df["BALANCE"]

mean_value = balance.mean()
median_value = balance.median()
mode_value = balance.mode()

print("\n--- ACCOUNT BALANCE STATISTICS ---")

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value.tolist())

print("Minimum:", balance.min())
print("Maximum:", balance.max())


# Variance and Standard Deviation

variance_value = balance.var()
std_value = balance.std()

print("\n--- VARIANCE & STANDARD DEVIATION ---")

print("Variance:", variance_value)
print("Standard Deviation:", std_value)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(9, 5))

sns.histplot(
    balance,
    bins=8,
    kde=True
)

plt.axvline(
    balance.mean(),
    linestyle="--",
    label="Mean"
)

plt.axvline(
    balance.median(),
    linestyle=":",
    label="Median"
)

plt.title("Account Balance Distribution")
plt.xlabel("Account Balance (BDT)")
plt.ylabel("Number of Accounts")
plt.legend()

plt.tight_layout()
plt.show()
