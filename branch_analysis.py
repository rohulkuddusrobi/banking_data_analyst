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

# Load Data
query = """
SELECT
    B.BRANCH_NAME,
    A.ACCOUNT_ID,
    A.BALANCE,
    A.ACCOUNT_TYPE
FROM BRANCHES B
JOIN CUSTOMERS C
    ON B.BRANCH_ID = C.BRANCH_ID
JOIN ACCOUNTS A
    ON C.CUSTOMER_ID = A.CUSTOMER_ID
"""

df = pd.read_sql(query, connection)

connection.close()

# Branch-wise Statistics
branch_summary = df.groupby("BRANCH_NAME").agg(
    TOTAL_ACCOUNTS=("ACCOUNT_ID", "count"),
    TOTAL_DEPOSIT=("BALANCE", "sum"),
    AVERAGE_BALANCE=("BALANCE", "mean"),
    MIN_BALANCE=("BALANCE", "min"),
    MAX_BALANCE=("BALANCE", "max")
).reset_index()

print("\n--- BRANCH-WISE ANALYSIS ---")
print(branch_summary.to_string(index=False))

# Chart
plt.figure(figsize=(10, 5))

sns.barplot(
    data=branch_summary,
    x="BRANCH_NAME",
    y="TOTAL_DEPOSIT"
)

plt.title("Branch-wise Total Account Balance")
plt.xlabel("Branch")
plt.ylabel("Total Balance (BDT)")
plt.xticks(rotation=25)

plt.tight_layout()
plt.show()
