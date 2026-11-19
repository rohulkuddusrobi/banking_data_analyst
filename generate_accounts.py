import os

import oracledb
import random
from datetime import datetime, timedelta

random.seed(42)

# Oracle Database Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

cursor = connection.cursor()

# Target
TARGET_ACCOUNTS = 70000
BATCH_SIZE = 2000

# Current Account Count and Maximum ID
cursor.execute("""
    SELECT COUNT(*), NVL(MAX(ACCOUNT_ID), 0)
    FROM ACCOUNTS
""")

current_count, max_id = cursor.fetchone()

print("Existing Accounts:", current_count)

if current_count >= TARGET_ACCOUNTS:
    print("Target already reached!")

else:
    # Load Customer IDs
    cursor.execute("SELECT CUSTOMER_ID FROM CUSTOMERS")
    customer_ids = [row[0] for row in cursor.fetchall()]

    account_types = [
        "SAVINGS",
        "CURRENT",
        "FIXED DEPOSIT"
    ]

    statuses = ["ACTIVE", "ACTIVE", "ACTIVE", "INACTIVE"]

    remaining = TARGET_ACCOUNTS - current_count
    inserted = 0
    batch = []

    while inserted < remaining:

        account_id = max_id + inserted + 1
        customer_id = random.choice(customer_ids)
        account_type = random.choice(account_types)

        opening_date = datetime.now() - timedelta(
            days=random.randint(30, 2500)
        )

        balance = round(random.uniform(5000, 500000), 2)
        status = random.choice(statuses)

        batch.append((
            account_id,
            customer_id,
            account_type,
            opening_date,
            balance,
            status
        ))

        inserted += 1

        if len(batch) >= BATCH_SIZE or inserted == remaining:

            cursor.executemany("""
                INSERT INTO ACCOUNTS (
                    ACCOUNT_ID,
                    CUSTOMER_ID,
                    ACCOUNT_TYPE,
                    OPENING_DATE,
                    BALANCE,
                    STATUS
                )
                VALUES (:1, :2, :3, :4, :5, :6)
            """, batch)

            connection.commit()

            print(f"Inserted: {inserted} / {remaining}")

            batch.clear()

    print("\nAccount Generation Completed!")

# Final Count
cursor.execute("SELECT COUNT(*) FROM ACCOUNTS")
print("Total Accounts:", cursor.fetchone()[0])

cursor.close()
connection.close()
