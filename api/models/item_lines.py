from api.models.base import Base

class ItemLines(Base):
    def __init__(self):
        super().__init__()

    def gets(self):
        """Retrieve all item lines."""
        query = "SELECT * FROM item_lines"
        return self.fetch_all(query)

    def get_item_line(self, line_id):
        """Retrieve a single item line by ID."""
        query = "SELECT * FROM item_lines WHERE id = ?"
        return self.fetch_one(query, (line_id,))

    def add_item_line(self, item_line):
        """Add a new item line."""
        query = """
        INSERT INTO item_lines (name, description, created_at, updated_at)
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

    def update_item_line(self, line_id, item_line):
        """Update an existing item line."""
        query = """
        UPDATE item_lines
        SET name = ?, description = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            item_line['name'],
            item_line['description'],
            self.get_timestamp(),
            line_id
        )
        self.execute_query(query, params)

    def remove_item_line(self, line_id):
        """Remove an item line by ID."""
        query = "DELETE FROM item_lines WHERE id = ?"
        self.execute_query(query, (line_id,))

