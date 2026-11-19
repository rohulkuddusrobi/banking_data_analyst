import os

import oracledb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to Oracle
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

# Count customers by city
city_counts = df["CITY"].value_counts()

print("\nCustomers by City:")
print(city_counts)

# Create Bar Chart
plt.figure(figsize=(9, 5))

sns.barplot(
    x=city_counts.index,
    y=city_counts.values
)

plt.title("Customer Distribution by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()

# Gender Distribution
gender_counts = df["GENDER"].value_counts()

print("\nCustomers by Gender:")
print(gender_counts)

# Create Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Gender Distribution")
plt.tight_layout()
plt.show()
