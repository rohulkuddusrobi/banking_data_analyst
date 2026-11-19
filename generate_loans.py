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

TARGET_LOANS = 20000
BATCH_SIZE = 2000

# Existing Loan Count and Maximum ID
cursor.execute("""
    SELECT COUNT(*), NVL(MAX(LOAN_ID), 0)
    FROM LOANS
""")

current_count, max_id = cursor.fetchone()

print("Existing Loans:", current_count)

if current_count >= TARGET_LOANS:
    print("Target already reached!")

else:
    # Load Customer IDs
    cursor.execute("SELECT CUSTOMER_ID FROM CUSTOMERS")
    customer_ids = [row[0] for row in cursor.fetchall()]

    loan_types = [
        "PERSONAL LOAN",
        "HOME LOAN",
        "BUSINESS LOAN",
        "CAR LOAN",
        "EDUCATION LOAN"
    ]

    statuses = ["ACTIVE", "ACTIVE", "ACTIVE", "CLOSED", "DEFAULTED"]

    remaining = TARGET_LOANS - current_count
    inserted = 0
    batch = []

    while inserted < remaining:

        loan_id = max_id + inserted + 1
        customer_id = random.choice(customer_ids)

        loan_type = random.choice(loan_types)
        loan_amount = round(random.uniform(50000, 5000000), 2)
        interest_rate = round(random.uniform(5, 15), 2)

        issue_date = datetime.now() - timedelta(
            days=random.randint(30, 1800)
        )

        due_date = issue_date + timedelta(
            days=random.choice([365, 730, 1095, 1825])
        )

        loan_status = random.choice(statuses)

        if loan_status == "DEFAULTED":
            is_defaulted = "Y"
        else:
            is_defaulted = "N"

        batch.append((
            loan_id,
            customer_id,
            loan_type,
            loan_amount,
            interest_rate,
            issue_date,
            due_date,
            loan_status,
            is_defaulted
        ))

        inserted += 1

        if len(batch) >= BATCH_SIZE or inserted == remaining:

            cursor.executemany("""
                INSERT INTO LOANS (
                    LOAN_ID,
                    CUSTOMER_ID,
                    LOAN_TYPE,
                    LOAN_AMOUNT,
                    INTEREST_RATE,
                    ISSUE_DATE,
                    DUE_DATE,
                    LOAN_STATUS,
                    IS_DEFAULTED
                )
                VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
            """, batch)

            connection.commit()

            print(f"Inserted: {inserted} / {remaining}")

            batch.clear()

    print("\nLoan Generation Completed!")

# Verify final count
cursor.execute("SELECT COUNT(*) FROM LOANS")

print("Total Loans:", cursor.fetchone()[0])

cursor.close()
connection.close()
