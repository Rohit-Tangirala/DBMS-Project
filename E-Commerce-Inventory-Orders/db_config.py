
import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="mysql-3a6fca03-klh-d8a.e.aivencloud.com",
        user="avnadmin",
        password="YOUR_AIVEN_PASSWORD",
        database="defaultdb",
        port=18589,
        ssl_disabled=False
    )
    return conn
