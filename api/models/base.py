import sqlite3
from datetime import datetime
import os

class Base:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, '../../ILY_TEST.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_timestamp(self):
        """Generate a timestamp in ISO 8601 format."""
        return datetime.utcnow().isoformat() + "Z"

    def execute_query(self, query, params=()):
        """Execute a SQL query with optional parameters."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def fetch_all(self, query, params=()):
        """Fetch all results from a SQL query."""
        cursor = self.execute_query(query, params)
        return cursor.fetchall() if cursor else []

    def fetch_one(self, query, params=()):
        """Fetch one result from a SQL query."""
        cursor = self.execute_query(query, params)
        return cursor.fetchone()

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

