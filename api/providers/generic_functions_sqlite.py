
import sqlite3
from datetime import datetime

class GenericFunctionsSQLite:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"

    def get_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_data_by_id(self, table_name, data_id):
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (data_id,))
        return self.cursor.fetchone()

    def add_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}, created_at, updated_at) VALUES ({placeholders}, ?, ?)"
        timestamp = self.get_timestamp()
        values = list(data.values()) + [timestamp, timestamp]
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_data(self, table_name, data_id, data):
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause}, updated_at = ? WHERE id = ?"
        values = list(data.values()) + [self.get_timestamp(), data_id]
        self.cursor.execute(query, values)
        self.conn.commit()

    def remove_data(self, table_name, data_id):
        query = f"DELETE FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (data_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
