
import oracledb
import pandas as pd
import os

os.makedirs("reports", exist_ok=True)

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

tables = {
    "BRANCHES": "SELECT * FROM BRANCHES",
    "CUSTOMERS": "SELECT * FROM CUSTOMERS",
    "ACCOUNTS": "SELECT * FROM ACCOUNTS",
    "TRANSACTIONS": "SELECT * FROM TRANSACTIONS",
    "LOANS": "SELECT * FROM LOANS"
}

report = []

for table_name, query in tables.items():

    df = pd.read_sql(query, connection)

    duplicates = df.duplicated().sum()
    missing = df.isnull().sum().sum()

    invalid_records = 0

    if table_name == "ACCOUNTS":
        invalid_records = (df["BALANCE"] < 0).sum()

    elif table_name == "TRANSACTIONS":
        invalid_records = (df["AMOUNT"] <= 0).sum()

    elif table_name == "LOANS":
        invalid_records = (df["LOAN_AMOUNT"] <= 0).sum()

    report.append({
        "TABLE": table_name,
        "TOTAL_RECORDS": len(df),
        "DUPLICATES": duplicates,
        "MISSING_VALUES": missing,
        "INVALID_RECORDS": invalid_records
    })

connection.close()

# Create Report
quality_report = pd.DataFrame(report)

print("\n--- AUTOMATED DATA QUALITY REPORT ---")
print(quality_report.to_string(index=False))

# Save CSV
quality_report.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

# Save Excel
quality_report.to_excel(
    "reports/data_quality_report.xlsx",
    index=False
)

print("\nData Quality Report Saved Successfully!")
