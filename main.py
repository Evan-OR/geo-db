import psycopg2
from utils.db_setup import create_tables, drop_all_tables


DB_NAME = "meetDB"
DB_USER = "admin"
DB_PASSWORD = "password123"
DB_HOST = "localhost"
DB_PORT = 5432


def connect():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )


if __name__ == "__main__":
    conn = connect()

    create_tables(conn)

    conn.close()
    print("Finished!")
