import os

import oracledb
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker("en_US")
random.seed(42)
Faker.seed(42)

TARGET_CUSTOMERS = 50000

locations = [
    ("Dhaka", "Dhaka"),
    ("Savar", "Dhaka"),
    ("Gazipur", "Gazipur"),
    ("Narayanganj", "Narayanganj"),
    ("Chattogram", "Chattogram"),
    ("Cumilla", "Cumilla"),
    ("Sylhet", "Sylhet"),
    ("Rajshahi", "Rajshahi"),
    ("Khulna", "Khulna"),
    ("Barishal", "Barishal"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
    ("Bogura", "Bogura"),
    ("Jashore", "Jashore"),
    ("Tangail", "Tangail")
]

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

cursor = connection.cursor()

# Existing Customer Information
cursor.execute("""
    SELECT COUNT(*), NVL(MAX(CUSTOMER_ID), 0)
    FROM CUSTOMERS
""")

current_count, max_id = cursor.fetchone()

remaining = TARGET_CUSTOMERS - current_count

if remaining <= 0:
    print("Target customer count already reached.")

else:

    # Get available Branch IDs
    cursor.execute("""
        SELECT BRANCH_ID
        FROM BRANCHES
        WHERE STATUS = 'ACTIVE'
    """)

    branch_ids = [row[0] for row in cursor.fetchall()]

    insert_query = """
        INSERT INTO CUSTOMERS (
            CUSTOMER_ID, FIRST_NAME, LAST_NAME,
            GENDER, DATE_OF_BIRTH, PHONE,
            EMAIL, CITY, DISTRICT, BRANCH_ID,
            REGISTRATION_DATE, STATUS
        )
        VALUES (
            :1, :2, :3, :4, :5, :6,
            :7, :8, :9, :10, :11, :12
        )
    """

    batch = []
    batch_size = 2000

    for i in range(remaining):

        customer_id = max_id + i + 1

        first_name = fake.first_name()
        last_name = fake.last_name()

        gender = random.choice(["Male", "Female"])

        dob = fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        )

        city, district = random.choice(locations)

        phone = f"01{random.randint(300000000, 999999999)}"

        email = f"customer{customer_id}@example.com"

        branch_id = random.choice(branch_ids)

        registration_date = fake.date_between(
            start_date="-5y",
            end_date="today"
        )

        batch.append((
            customer_id,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            city,
            district,
            branch_id,
            registration_date,
            "ACTIVE"
        ))

        if len(batch) >= batch_size:
            cursor.executemany(insert_query, batch)
            connection.commit()
            batch.clear()

            print(f"Inserted: {i + 1} / {remaining}")

    if batch:
        cursor.executemany(insert_query, batch)
        connection.commit()

    print("Customer Generation Completed!")

# Verify
cursor.execute("SELECT COUNT(*) FROM CUSTOMERS")
total = cursor.fetchone()[0]

print("Total Customers:", total)

cursor.close()
connection.close()
