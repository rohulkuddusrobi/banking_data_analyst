
import os
import oracledb

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()


# Direct Oracle connection (for insert, update, cursor operations)
def get_connection():
    return oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )


# SQLAlchemy engine (for Pandas read_sql operations)
def get_engine():

    url = URL.create(
        "oracle+oracledb",
        username=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        host="localhost",
        port=1521,
        query={"service_name": "FREEPDB1"}
    )

    return create_engine(url)
