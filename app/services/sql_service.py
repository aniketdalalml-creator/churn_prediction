import os
import psycopg2
from dotenv import load_dotenv

# Optional: useful for local dev, safe to keep
load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("SUPABASE_DB_HOST"),
        port=int(os.getenv("SUPABASE_DB_PORT")),
        dbname=os.getenv("SUPABASE_DB_NAME"),
        user=os.getenv("SUPABASE_DB_USER"),
        password=os.getenv("SUPABASE_DB_PASSWORD"),
        sslmode="require"  # 🔥 REQUIRED for Supabase
    )


def fetch_query(query: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    return colnames, rows


def get_churn_summary():
    query = """
        SELECT month, total_customers, churned_customers, churn_rate
        FROM churn_summary
        ORDER BY month;
    """
    return fetch_query(query)