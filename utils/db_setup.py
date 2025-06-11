from psycopg2.extensions import connection

CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  display_name VARCHAR(100),
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  password_hash TEXT NOT NULL,
  date_of_birth DATE,
  description TEXT,
  job VARCHAR(100),
  gender_id INTEGER REFERENCES genders(id),
  interested_in_gender_id INTEGER REFERENCES genders(id),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
"""

CREATE_GENDER_TABLE = """
CREATE TABLE genders (
  id SERIAL PRIMARY KEY,
  label VARCHAR(50) UNIQUE NOT NULL
);
"""
# 'All' in gender list is just for specifying [interested_in_gender_id] column in user table
POPULATE_GENDER_TABLE = """
INSERT INTO genders (label) VALUES
('Male'),
('Female'),
('Non-binary'),
('Other'),
('All')
ON CONFLICT (label) DO NOTHING;
"""


def create_tables(conn: connection):
    with conn.cursor() as cur:
        cur.execute(CREATE_GENDER_TABLE)
        cur.execute(POPULATE_GENDER_TABLE)
        print(f"Created gender table")

        cur.execute(CREATE_USER_TABLE)
        print(f"Created user table")

    conn.commit()


def drop_all_tables(conn: connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE';
        """
        )
        tables = cur.fetchall()

        for (table,) in tables:
            if table == "spatial_ref_sys":
                continue

            print(f"Dropping table: {table}")
            cur.execute(f"DROP TABLE IF EXISTS {table} CASCADE;")

    conn.commit()
    print("All tables dropped.")
