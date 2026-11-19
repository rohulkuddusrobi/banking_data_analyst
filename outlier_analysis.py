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

df = pd.read_sql("""
    SELECT TRANSACTION_ID, AMOUNT
    FROM TRANSACTIONS
    WHERE STATUS = 'SUCCESS'
""", connection)

connection.close()

# Calculate IQR
Q1 = df["AMOUNT"].quantile(0.25)
Q3 = df["AMOUNT"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

# Detect Outliers
outliers = df[
    (df["AMOUNT"] < lower_limit) |
    (df["AMOUNT"] > upper_limit)
]

print("\n--- OUTLIER ANALYSIS ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nTotal Transactions:", len(df))
print("Outlier Count:", len(outliers))

print("\n--- OUTLIER RECORDS ---")
print(outliers.to_string(index=False))

# Boxplot
plt.figure(figsize=(9, 4))

sns.boxplot(x=df["AMOUNT"])

plt.title("Transaction Amount Outlier Detection")
plt.xlabel("Transaction Amount (BDT)")

plt.tight_layout()
plt.show()
