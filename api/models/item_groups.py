from api.models.base import Base
from api.providers import data_provider

class ItemGroups(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all item groups."""
        query = "SELECT * FROM item_groups"
        return self.fetch_all(query)

    def get(self, item_group_id):
        """Retrieve a single item group by ID."""
        query = "SELECT * FROM item_groups WHERE id = ?"
        return self.fetch_one(query, (item_group_id,))

    def add(self, item_group):
        """Add a new item group."""
        query = """
        INSERT INTO item_groups (name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item_group.get('name', None),
            item_group.get('description', None),
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, item_group_id, item_group):
        """Update an existing item group."""
        query = """
        UPDATE item_groups
        SET name = ?, description = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            item_group.get('name', None),
            item_group.get('description', None),
            self.get_timestamp(),
            item_group_id
        )
        self.execute_query(query, params)

    def remove(self, item_group_id):
        """Remove an item group by ID."""
        query = "DELETE FROM item_groups WHERE id = ?"
        self.execute_query(query, (item_group_id,))


