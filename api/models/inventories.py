from api.models.base import Base

class Inventories(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all inventories."""
        query = "SELECT * FROM inventories"
        return self.fetch_all(query)

    def get(self, inventory_id):
        """Retrieve a single inventory by ID."""
        query = "SELECT * FROM inventories WHERE id = ?"
        return self.fetch_one(query, (inventory_id,))

    def get_inventories_for_item(self, item_id):
        """Retrieve all inventories for a specific item ID."""
        query = "SELECT * FROM inventories WHERE item_id = ?"
        return self.fetch_all(query, (item_id,))

    def get_inventory_totals_for_item(self, item_id):
        """Calculate totals for a specific item ID."""
        query = """
        SELECT 
            SUM(total_expected) as total_expected,
            SUM(total_ordered) as total_ordered,
            SUM(total_allocated) as total_allocated,
            SUM(total_available) as total_available
        FROM inventories
        WHERE item_id = ?
        """
        return self.fetch_one(query, (item_id,))

    def add_inventory(self, inventory):
        """Add a new inventory record."""
        query = """
        INSERT INTO inventories (item_id, location_id, total_expected, total_ordered, total_allocated, total_available, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            inventory['item_id'],
            inventory['location_id'],
            inventory['total_expected'],
            inventory['total_ordered'],
            inventory['total_allocated'],
            inventory['total_available'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_inventory(self, inventory_id, inventory):
        """Update an existing inventory record."""
        query = """
        UPDATE inventories
        SET item_id = ?, location_id = ?, total_expected = ?, total_ordered = ?,
            total_allocated = ?, total_available = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            inventory['item_id'],
            inventory['location_id'],
            inventory['total_expected'],
            inventory['total_ordered'],
            inventory['total_allocated'],
            inventory['total_available'],
            self.get_timestamp(),
            inventory_id
        )
        self.execute_query(query, params)

    def remove_inventory(self, inventory_id):
        """Remove an inventory record by ID."""
        query = "DELETE FROM inventories WHERE id = ?"
        self.execute_query(query, (inventory_id,))

