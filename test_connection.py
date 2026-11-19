import os

import oracledb

try:
    connection = oracledb.connect(
        user=os.getenv("ORACLE_USER", "BANKING_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN", "localhost:1521/FREEPDB1")
    )

    print("Oracle Database Connected Successfully!")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT USER,
               SYS_CONTEXT('USERENV', 'CON_NAME')
        FROM DUAL
    """)

    result = cursor.fetchone()

    print("Connected User:", result[0])
    print("Container Name:", result[1])

    cursor.close()
    connection.close()

except Exception as e:
    print("Connection Failed:", e)
