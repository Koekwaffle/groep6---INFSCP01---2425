from api.models.base import Base

class ItemGroups(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all item groups."""
        query = "SELECT * FROM item_groups"
        return self.fetch_all(query)

    def get(self, group_id):
        """Retrieve a single item group by ID."""
        query = "SELECT * FROM item_groups WHERE id = ?"
        return self.fetch_one(query, (group_id,))

    def add_item_group(self, item_group):
        """Add a new item group."""
        query = """
        INSERT INTO item_groups (name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item_group['name'],
            item_group['description'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_item_group(self, group_id, item_group):
        """Update an existing item group."""
        query = """
        UPDATE item_groups
        SET name = ?, description = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            item_group['name'],
            item_group['description'],
            self.get_timestamp(),
            group_id
        )
        self.execute_query(query, params)

    def remove_item_group(self, group_id):
        """Remove an item group by ID."""
        query = "DELETE FROM item_groups WHERE id = ?"
        self.execute_query(query, (group_id,))


