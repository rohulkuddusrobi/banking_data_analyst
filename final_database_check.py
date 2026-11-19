
from db_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

print("\n===== DATABASE FINAL VERIFICATION =====")

cursor.execute("""
    SELECT USER, SYS_CONTEXT('USERENV', 'CON_NAME')
    FROM DUAL
""")

user, container = cursor.fetchone()

print("Connected User:", user)
print("Database:", container)

tables = {
    "BRANCHES": 100,
    "CUSTOMERS": 50000,
    "ACCOUNTS": 70000,
    "TRANSACTIONS": 300000,
    "LOANS": 20000
}

all_passed = True

print("\n----- TABLE RECORD COUNTS -----")

for table, expected in tables.items():
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    actual = cursor.fetchone()[0]

    status = "PASS" if actual == expected else "CHECK"

    if actual != expected:
        all_passed = False

    print(
        f"{table}: {actual:,} / "
        f"{expected:,} [{status}]"
    )

print("\nTotal Expected Records:", sum(tables.values()))

if all_passed:
    print("\nDATABASE VERIFICATION SUCCESSFUL!")
else:
    print("\nDATABASE VERIFICATION NEEDS REVIEW!")

cursor.close()
connection.close()
