
from db_connection import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
    SELECT USER, SYS_CONTEXT('USERENV', 'CON_NAME')
    FROM DUAL
""")

result = cursor.fetchone()

print("Reusable Connection Successful!")
print("User:", result[0])
print("Container:", result[1])

cursor.close()
connection.close()
