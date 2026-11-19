import os

import oracledb
import pandas as pd

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

df = pd.read_sql("SELECT * FROM CUSTOMERS", connection)

# 1. Dataset Shape
print("\n--- DATASET SHAPE ---")
print(df.shape)

# 2. Column Names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 3. Data Types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 4. Missing Values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 5. Statistical Summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include="all"))

connection.close()
