import mysql.connector
import os

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql-3a6fca03-klh-d8a.e.aivencloud.com"),
        user=os.getenv("MYSQL_USER", "avnadmin"),
        password=os.getenv("MYSQL_PASSWORD", "AVNS_h4WPyDDaI1AaWyc1jWW"),
        database=os.getenv("MYSQL_DB", "defaultdb"),
        port=int(os.getenv("MYSQL_PORT", 18589))
    )
    return conn
