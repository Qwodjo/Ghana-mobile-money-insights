import os

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor


# Load environment variables from .env in the project root
load_dotenv()


def get_connection():
	"""Create and return a connection to the Ghana_momo PostgreSQL database.

	Connection details come from environment variables (usually via .env):
	- PGHOST (default: localhost)
	- PGPORT (default: 5432)
	- PGUSER (default: postgres)
	- PGPASSWORD (no default, must be set if required)
	- PGDATABASE (default: Ghana_momo)
	"""

	host = os.getenv("PGHOST", "localhost")
	port = int(os.getenv("PGPORT", "5432"))
	user = os.getenv("PGUSER", "postgres")
	password = os.getenv("PGPASSWORD")
	dbname = os.getenv("PGDATABASE", "Ghana_momo")

	conn = psycopg2.connect(
		host=host,
		port=port,
		user=user,
		password=password,
		dbname=dbname,
	)
	return conn


def get_dict_cursor(conn):
	"""Return a cursor that yields rows as dictionaries."""
	return conn.cursor(cursor_factory=RealDictCursor)


def test_connection():
	"""Simple helper to test that the DB connection works."""
	conn = get_connection()
	cur = get_dict_cursor(conn)
	cur.execute("SELECT current_database() AS db, current_user AS usr;")
	row = cur.fetchone()
	print(f"Connected to database: {row['db']} as user: {row['usr']}")
	cur.close()
	conn.close()
	print("Connection OK")


if __name__ == "__main__":
	test_connection()


