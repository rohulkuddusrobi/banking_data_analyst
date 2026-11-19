import os

import oracledb
import pandas as pd

# Oracle Database Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

# Load Customer Data
df = pd.read_sql(
    "SELECT * FROM CUSTOMERS",
    connection
)

connection.close()

# Check Duplicate Records
print("Total Records:", len(df))

print(
    "Duplicate Records:",
    df.duplicated().sum()
)

# Display Duplicate Rows
duplicates = df[df.duplicated(keep=False)]

print("\nDuplicate Records:")
print(duplicates)

# Check Missing Values
print("\n--- MISSING VALUE ANALYSIS ---")

missing_values = df.isnull().sum()

print(missing_values)

print(
    "\nTotal Missing Values:",
    missing_values.sum()
)

# Check Data Types
print("\n--- DATA TYPE VALIDATION ---")

print(df.dtypes)

# Check Date Columns
print("\n--- DATE COLUMN VALIDATION ---")

print("DATE_OF_BIRTH:", df["DATE_OF_BIRTH"].dtype)

print("REGISTRATION_DATE:", df["REGISTRATION_DATE"].dtype)


# Outlier Detection in Account Balance

accounts_df = pd.read_sql(
    "SELECT * FROM ACCOUNTS",
    oracledb.connect(
        user=os.getenv("ORACLE_USER", "BANKING_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
    )
)

Q1 = accounts_df["BALANCE"].quantile(0.25)
Q3 = accounts_df["BALANCE"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = accounts_df[
    (accounts_df["BALANCE"] < lower_limit) |
    (accounts_df["BALANCE"] > upper_limit)
]

print("\n--- OUTLIER ANALYSIS ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nOutlier Records:")
print(outliers[["ACCOUNT_ID", "BALANCE"]])

print("\nTotal Outliers:", len(outliers))


# Invalid Age Detection

from datetime import date

today = pd.Timestamp.today().normalize()

df["AGE"] = (
    (today - df["DATE_OF_BIRTH"]).dt.days / 365.25
).astype(int)

invalid_age = df[
    (df["AGE"] < 18) |
    (df["AGE"] > 100)
]

print("\n--- INVALID AGE ANALYSIS ---")

print("Total Customers:", len(df))

print("\nInvalid Age Records:")

print(
    invalid_age[
        ["CUSTOMER_ID", "FIRST_NAME", "DATE_OF_BIRTH", "AGE"]
    ]
)

print("\nTotal Invalid Ages:", len(invalid_age))


# Transaction Data Cleaning

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

transactions_df = pd.read_sql(
    "SELECT * FROM TRANSACTIONS",
    connection
)

connection.close()

print("\n--- TRANSACTION DATA QUALITY ---")

# Total Records
print("Total Transactions:", len(transactions_df))

# Duplicate Records
print(
    "Duplicate Records:",
    transactions_df.duplicated().sum()
)

# Missing Values
print(
    "\nMissing Values:\n",
    transactions_df.isnull().sum()
)

# Invalid Amount
invalid_amount = transactions_df[
    transactions_df["AMOUNT"] <= 0
]

print("\nInvalid Transaction Amounts:")
print(invalid_amount)

print("Total Invalid Amounts:", len(invalid_amount))


# Transaction Date Validation

future_transactions = transactions_df[
    transactions_df["TRANSACTION_DATE"] > pd.Timestamp.now()
]

print("\n--- FUTURE TRANSACTION CHECK ---")
print(future_transactions)

# Transaction Type Validation

valid_types = [
    "DEPOSIT",
    "WITHDRAWAL",
    "TRANSFER"
]

invalid_types = transactions_df[
    ~transactions_df["TRANSACTION_TYPE"].isin(valid_types)
]

print("\n--- INVALID TRANSACTION TYPES ---")
print(invalid_types)

# Channel Validation

valid_channels = [
    "BRANCH",
    "ATM",
    "MOBILE BANKING",
    "INTERNET BANKING"
]

invalid_channels = transactions_df[
    ~transactions_df["CHANNEL"].isin(valid_channels)
]

print("\n--- INVALID TRANSACTION CHANNELS ---")
print(invalid_channels)

print("\nTotal Invalid Types:", len(invalid_types))
print("Total Invalid Channels:", len(invalid_channels))
print("Total Future Transactions:", len(future_transactions))


# Loan Data Cleaning

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

loans_df = pd.read_sql(
    "SELECT * FROM LOANS",
    connection
)

connection.close()

print("\n--- LOAN DATA QUALITY ---")

# Total Records
print("Total Loans:", len(loans_df))

# Duplicate Records
print(
    "Duplicate Records:",
    loans_df.duplicated().sum()
)

# Missing Values
print("\nMissing Values:")
print(loans_df.isnull().sum())

# Invalid Loan Amount
invalid_amount = loans_df[
    loans_df["LOAN_AMOUNT"] <= 0
]

# Invalid Interest Rate
invalid_interest = loans_df[
    (loans_df["INTEREST_RATE"] < 0) |
    (loans_df["INTEREST_RATE"] > 100)
]

# Invalid Loan Status
valid_status = ["ACTIVE", "CLOSED", "DEFAULTED"]

invalid_status = loans_df[
    ~loans_df["LOAN_STATUS"].isin(valid_status)
]

# Invalid Default Flag
invalid_default = loans_df[
    ~loans_df["IS_DEFAULTED"].isin(["Y", "N"])
]

print("\nInvalid Loan Amounts:", len(invalid_amount))
print("Invalid Interest Rates:", len(invalid_interest))
print("Invalid Loan Status:", len(invalid_status))
print("Invalid Default Flags:", len(invalid_default))


# Overall Data Quality Summary

tables = {
    "BRANCHES": "SELECT * FROM BRANCHES",
    "CUSTOMERS": "SELECT * FROM CUSTOMERS",
    "ACCOUNTS": "SELECT * FROM ACCOUNTS",
    "TRANSACTIONS": "SELECT * FROM TRANSACTIONS",
    "LOANS": "SELECT * FROM LOANS"
}

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

summary = []

for table_name, query in tables.items():

    data = pd.read_sql(query, connection)

    summary.append({
        "TABLE": table_name,
        "TOTAL_RECORDS": len(data),
        "DUPLICATES": data.duplicated().sum(),
        "MISSING_VALUES": data.isnull().sum().sum()
    })

connection.close()

summary_df = pd.DataFrame(summary)

print("\n--- OVERALL DATA QUALITY REPORT ---")
print(summary_df.to_string(index=False))

print("\nTotal Database Records:", summary_df["TOTAL_RECORDS"].sum())
print("Total Duplicates:", summary_df["DUPLICATES"].sum())
print("Total Missing Values:", summary_df["MISSING_VALUES"].sum())
