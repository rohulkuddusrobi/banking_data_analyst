
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from db_connection import get_engine


# =====================================
# 1. DATABASE CONNECTION
# =====================================

print("Connecting to Oracle Database...")

engine = get_engine()

with engine.connect() as connection:
    df = pd.read_sql(
        "SELECT * FROM ACCOUNTS",
        connection
    )

engine.dispose()

# Convert column names to uppercase
df.columns = df.columns.str.upper()

print("Account data loaded successfully!")
print("Total Records:", len(df))


# =====================================
# 2. ACCOUNT TYPE DISTRIBUTION
# =====================================

account_counts = df["ACCOUNT_TYPE"].value_counts()

print("\n--- ACCOUNT TYPE DISTRIBUTION ---")
print(account_counts)


# =====================================
# 3. TOTAL BALANCE BY ACCOUNT TYPE
# =====================================

balance_summary = df.groupby(
    "ACCOUNT_TYPE"
)["BALANCE"].sum().sort_values(ascending=False)

print("\n--- TOTAL BALANCE BY ACCOUNT TYPE ---")
print(balance_summary)


# =====================================
# 4. OVERALL ACCOUNT STATISTICS
# =====================================

print("\n--- ACCOUNT STATISTICS ---")

print("Total Balance:", df["BALANCE"].sum())

print("Average Balance:", df["BALANCE"].mean())

print("Minimum Balance:", df["BALANCE"].min())

print("Maximum Balance:", df["BALANCE"].max())


# =====================================
# 5. VISUALIZATION
# =====================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=balance_summary.index,
    y=balance_summary.values
)

plt.title("Total Balance by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Total Balance (BDT)")

plt.tight_layout()

plt.show()


print("\nAccount Analysis Completed Successfully!")
