import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv


load_dotenv()


def _get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432)),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def get_schema(table_name):
    """Fetches the schema from table
        Return : dict """
    
    conn = _get_connection()
    curr = conn.cursor()
    query = """
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_name = %s
    """
    curr.execute(query, (table_name,))
    rows = curr.fetchall()
    schema = {}

    for row in rows:
        schema[row[0]] = {"type": row[1], "nullable": row[2]}

    return schema