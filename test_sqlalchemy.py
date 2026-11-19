
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

# Create Oracle connection URL
url = URL.create(
    "oracle+oracledb",
    username=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    host="localhost",
    port=1521,
    query={"service_name": "FREEPDB1"}
)

# Create SQLAlchemy engine
engine = create_engine(url)

# Test connection
with engine.connect() as connection:
    result = connection.execute(
        text("""
            SELECT USER,
                   SYS_CONTEXT('USERENV', 'CON_NAME')
            FROM DUAL
        """)
    )

    row = result.fetchone()

    print("SQLAlchemy Connection Successful!")
    print("Connected User:", row[0])
    print("Database Container:", row[1])

engine.dispose()
