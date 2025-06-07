from datetime import datetime, date
from psycopg2.extensions import connection

TEST_USERS = [
    {
        "email": "evan@example.com",
        "name": "Evan",
        "password_hash": "$2b$10$NSoIeNiNKwCM2Wqe9YIWAuCOmtYhruVrXxpRo3D.amp9aTvQ33gwa",  # plaintext password = 123
        "date_of_birth": date(2000, 10, 18),
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultrices semper urna, nec interdum ante laoreet eget.",
        "job": "Software Engineer",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    },
    {
        "email": "kev@example.com",
        "name": "Kevin",
        "password_hash": "$2b$10$NSoIeNiNKwCM2Wqe9YIWAuCOmtYhruVrXxpRo3D.amp9aTvQ33gwa",  # plaintext password = 123
        "date_of_birth": date(2001, 12, 20),
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultrices semper urna, nec interdum ante laoreet eget.",
        "job": "Founder",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    },
]


def insert_test_users(conn: connection) -> None:
    with conn:
        with conn.cursor() as cur:
            for user in TEST_USERS:
                cur.execute(
                    f"""
                    INSERT INTO users (email, name, password_hash, date_of_birth, description, job, created_at, updated_at)
                    VALUES (
                    '{user["email"]}',
                    '{user["name"]}',
                    '{user["password_hash"]}',
                    '{user["date_of_birth"]}',
                    '{user["description"]}',
                    '{user["job"]}',
                    '{user["created_at"]}',
                    '{user["updated_at"]}'
                    );
                    """
                )
