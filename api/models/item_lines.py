from api.models.base import Base
from api.providers import data_provider

class ItemLines(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all item lines."""
        query = "SELECT * FROM item_line"
        return self.fetch_all(query)

    def get(self, item_line_id):
        """Retrieve a single item line by ID."""
        query = "SELECT * FROM item_line WHERE id = ?"
        return self.fetch_one(query, (item_line_id,))

    def add(self, item_line):
        """Add a new item line."""
        query = """
        INSERT INTO item_line (name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item_line['name'],
            item_line['description'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, item_line_id, item_line):
        """Update an existing item line."""
        query = """
        UPDATE item_line
        SET name = ?, description = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            item_line['name'],
            item_line['description'],
            self.get_timestamp(),
            item_line_id
        )
        self.execute_query(query, params)

    def remove(self, item_line_id):
        """Remove an item line by ID."""
        query = "DELETE FROM item_line WHERE id = ?"
        self.execute_query(query, (item_line_id,))

