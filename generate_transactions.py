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

TARGET_TRANSACTIONS = 300000
BATCH_SIZE = 5000

# Current count and maximum ID
cursor.execute("""
    SELECT COUNT(*), NVL(MAX(TRANSACTION_ID), 0)
    FROM TRANSACTIONS
""")

current_count, max_id = cursor.fetchone()

print("Existing Transactions:", current_count)

if current_count >= TARGET_TRANSACTIONS:
    print("Target already reached!")

else:
    # Load Account IDs
    cursor.execute("SELECT ACCOUNT_ID FROM ACCOUNTS")
    account_ids = [row[0] for row in cursor.fetchall()]

    transaction_types = [
        "DEPOSIT",
        "WITHDRAWAL",
        "TRANSFER"
    ]

    channels = [
        "BRANCH",
        "ATM",
        "MOBILE BANKING",
        "INTERNET BANKING"
    ]

    statuses = [
        "SUCCESS",
        "SUCCESS",
        "SUCCESS",
        "SUCCESS",
        "FAILED",
        "REVERSED"
    ]

    remaining = TARGET_TRANSACTIONS - current_count
    inserted = 0
    batch = []

    while inserted < remaining:

        transaction_id = max_id + inserted + 1
        account_id = random.choice(account_ids)

        transaction_date = datetime.now() - timedelta(
            days=random.randint(0, 730),
            seconds=random.randint(0, 86399)
        )

        transaction_type = random.choice(transaction_types)
        amount = round(random.uniform(100, 200000), 2)
        channel = random.choice(channels)
        status = random.choice(statuses)

        batch.append((
            transaction_id,
            account_id,
            transaction_date,
            transaction_type,
            amount,
            channel,
            status
        ))

        inserted += 1

        if len(batch) >= BATCH_SIZE or inserted == remaining:

            cursor.executemany("""
                INSERT INTO TRANSACTIONS (
                    TRANSACTION_ID,
                    ACCOUNT_ID,
                    TRANSACTION_DATE,
                    TRANSACTION_TYPE,
                    AMOUNT,
                    CHANNEL,
                    STATUS
                )
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, batch)

            connection.commit()

            print(f"Inserted: {inserted} / {remaining}")

            batch.clear()

    print("\nTransaction Generation Completed!")

# Verify final count
cursor.execute("SELECT COUNT(*) FROM TRANSACTIONS")

print("Total Transactions:", cursor.fetchone()[0])

cursor.close()
connection.close()
