from models.base import Base

class Items(Base):
    def __init__(self):
        super().__init__()

    def get_items(self):
        """Retrieve all items."""
        query = "SELECT * FROM items"
        return self.fetch_all(query)

    def get_item(self, item_id):
        """Retrieve a single item by ID."""
        query = "SELECT * FROM items WHERE uid = ?"
        return self.fetch_one(query, (item_id,))

    def get_items_for_item_line(self, item_line_id):
        """Retrieve all items for a specific item line ID."""
        query = "SELECT * FROM items WHERE item_line = ?"
        return self.fetch_all(query, (item_line_id,))

    def get_items_for_item_group(self, item_group_id):
        """Retrieve all items for a specific item group ID."""
        query = "SELECT * FROM items WHERE item_group = ?"
        return self.fetch_all(query, (item_group_id,))

    def get_items_for_item_type(self, item_type_id):
        """Retrieve all items for a specific item type ID."""
        query = "SELECT * FROM items WHERE item_type = ?"
        return self.fetch_all(query, (item_type_id,))

    def get_items_for_supplier(self, supplier_id):
        """Retrieve all items for a specific supplier ID."""
        query = "SELECT * FROM items WHERE supplier_id = ?"
        return self.fetch_all(query, (supplier_id,))

    def add_item(self, item):
        """Add a new item."""
        query = """
        INSERT INTO items (name, item_line, item_group, item_type, supplier_id, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item['name'],
            item['item_line'],
            item['item_group'],
            item['item_type'],
            item['supplier_id'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_item(self, item_id, item):
        """Update an existing item."""
        query = """
        UPDATE items
        SET name = ?, item_line = ?, item_group = ?, item_type = ?, supplier_id = ?, updated_at = ?
        WHERE uid = ?
        """
        params = (
            item['name'],
            item['item_line'],
            item['item_group'],
            item['item_type'],
            item['supplier_id'],
            self.get_timestamp(),
            item_id
        )
        self.execute_query(query, params)

    def remove_item(self, item_id):
        """Remove an item by ID."""
        query = "DELETE FROM items WHERE uid = ?"
        self.execute_query(query, (item_id,))
