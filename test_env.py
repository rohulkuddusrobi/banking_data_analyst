
import os
import oracledb
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Oracle
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN")
)

cursor = connection.cursor()

cursor.execute("""
    SELECT USER, SYS_CONTEXT('USERENV', 'CON_NAME')
    FROM DUAL
""")

result = cursor.fetchone()

print("Connection Successful!")
print("Connected User:", result[0])
print("Database Container:", result[1])

cursor.close()
connection.close()
