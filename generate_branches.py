import os

import oracledb
import random
from faker import Faker

fake = Faker("en_US")
random.seed(42)

# Bangladesh locations
locations = [
    ("Dhaka", "Dhaka"),
    ("Savar", "Dhaka"),
    ("Gazipur", "Gazipur"),
    ("Narayanganj", "Narayanganj"),
    ("Chattogram", "Chattogram"),
    ("Cox's Bazar", "Cox's Bazar"),
    ("Cumilla", "Cumilla"),
    ("Sylhet", "Sylhet"),
    ("Rajshahi", "Rajshahi"),
    ("Khulna", "Khulna"),
    ("Barishal", "Barishal"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
    ("Bogura", "Bogura"),
    ("Jashore", "Jashore"),
    ("Tangail", "Tangail"),
    ("Feni", "Feni"),
    ("Pabna", "Pabna"),
    ("Dinajpur", "Dinajpur"),
    ("Kushtia", "Kushtia")
]

# Oracle Connection
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER", "BANKING_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
)

cursor = connection.cursor()

# Check existing branches
cursor.execute("""
    SELECT COUNT(*), NVL(MAX(BRANCH_ID), 0)
    FROM BRANCHES
""")

current_count, max_id = cursor.fetchone()

target_count = 100
remaining = target_count - current_count

if remaining <= 0:
    print("Already have 100 or more branches.")
else:

    branch_data = []

    for i in range(remaining):

        branch_id = max_id + i + 1

        city, district = random.choice(locations)

        branch_name = f"{city} Branch {branch_id}"

        opening_date = fake.date_between(
            start_date="-10y",
            end_date="today"
        )

        branch_data.append((
            branch_id,
            branch_name,
            city,
            district,
            opening_date,
            "ACTIVE"
        ))

    # Bulk Insert
    cursor.executemany("""
        INSERT INTO BRANCHES
        (BRANCH_ID, BRANCH_NAME, CITY,
         DISTRICT, OPENING_DATE, STATUS)
        VALUES (:1, :2, :3, :4, :5, :6)
    """, branch_data)

    connection.commit()

    print(f"New Branches Created: {remaining}")

# Verify
cursor.execute("SELECT COUNT(*) FROM BRANCHES")
total = cursor.fetchone()[0]

print("Total Branches in Database:", total)

cursor.close()
connection.close()

print("Branch Generation Completed!")
