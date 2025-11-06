import mysql.connector
import os


def get_db_connection():
    # Read configuration from environment variables only. Do NOT keep secrets in source code.
    host = os.getenv("MYSQL_HOST", "mysql-3a6fca03-klh-d8a.e.aivencloud.com")
    user = os.getenv("MYSQL_USER", "avnadmin")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DB", "defaultdb")
    port = int(os.getenv("MYSQL_PORT", 18589))

    if not password:
        # Fail fast with a clear message so deployments don't accidentally use an empty password.
        raise RuntimeError(
            "Missing required environment variable MYSQL_PASSWORD. Do NOT store the database password in source control."
        )

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
    )
    return conn
