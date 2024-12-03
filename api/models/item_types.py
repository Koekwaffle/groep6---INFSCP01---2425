from models.base import Base

class ItemTypes(Base):
    def __init__(self):
        super().__init__()

    def get_item_types(self):
        """Retrieve all item types."""
        query = "SELECT * FROM item_types"
        return self.fetch_all(query)

    def get_item_type(self, type_id):
        """Retrieve a single item type by ID."""
        query = "SELECT * FROM item_types WHERE id = ?"
        return self.fetch_one(query, (type_id,))

    def add_item_type(self, item_type):
        """Add a new item type."""
        query = """
        INSERT INTO item_types (name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item_type['name'],
            item_type['description'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_item_type(self, type_id, item_type):
        """Update an existing item type."""
        query = """
        UPDATE item_types
        SET name = ?, description = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            item_type['name'],
            item_type['description'],
            self.get_timestamp(),
            type_id
        )
        self.execute_query(query, params)

    def remove_item_type(self, type_id):
        """Remove an item type by ID."""
        query = "DELETE FROM item_types WHERE id = ?"
        self.execute_query(query, (type_id,))

