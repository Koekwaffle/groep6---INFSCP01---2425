from api.models.base import Base
from api.providers import data_provider

class Inventories(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

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

    def add(self, inventory):
        """Add a new inventory record."""
        query = """
        INSERT INTO inventories (item_id, location_id, total_expected, total_ordered, total_allocated, total_available, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            inventory['item_id'],
            inventory.get('location_id', None),
            inventory['total_expected'],
            inventory['total_ordered'],
            inventory['total_allocated'],
            inventory['total_available'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, inventory_id, inventory):
        """Update an existing inventory record."""
        query = """
        UPDATE inventories
        SET item_id = ?, location_id = ?, total_expected = ?, total_ordered = ?,
            total_allocated = ?, total_available = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            inventory['item_id'],
            inventory.get('location_id', None),
            inventory['total_expected'],
            inventory['total_ordered'],
            inventory['total_allocated'],
            inventory['total_available'],
            self.get_timestamp(),
            inventory_id
        )
        self.execute_query(query, params)

    def remove(self, inventory_id):
        """Remove an inventory record by ID."""
        query = "DELETE FROM inventories WHERE id = ?"
        self.execute_query(query, (inventory_id,))

    def get_by_item(self, item_uid):
        """Get all inventory records for a specific item"""
        try:
            query = """
            SELECT id, item_id, warehouse_id, location_id, quantity,
                   reserved_quantity, available_quantity, damaged_quantity,
                   created_at, updated_at
            FROM inventories 
            WHERE item_id = ?
            """
            inventories = self.fetch_all(query, (item_uid,))
            if inventories:
                inventory_dicts = [self.tuple_to_dict(inv) for inv in inventories]
                return [inv for inv in inventory_dicts if inv is not None]
            return None
        except Exception as e:
            print(f"Error getting inventories by item: {e}")
            return None

    def get_inventory_totals(self, item_uid):
        """Get inventory totals for a specific item"""
        try:
            query = """
            SELECT 
                SUM(quantity) as total_quantity,
                SUM(reserved_quantity) as total_reserved,
                SUM(available_quantity) as total_available,
                SUM(damaged_quantity) as total_damaged
            FROM inventories 
            WHERE item_id = ?
            """
            totals = self.fetch_one(query, (item_uid,))
            if totals:
                return {
                    'total_quantity': str(totals[0] or 0),
                    'total_reserved': str(totals[1] or 0),
                    'total_available': str(totals[2] or 0),
                    'total_damaged': str(totals[3] or 0)
                }
            return None
        except Exception as e:
            print(f"Error getting inventory totals: {e}")
            return None

    def tuple_to_dict(self, inventory_tuple):
        """Convert a tuple to a dictionary with named fields"""
        try:
            return {
                'id': str(inventory_tuple[0]),
                'item_id': str(inventory_tuple[1]),  # Changed from item_uid to item_id
                'warehouse_id': str(inventory_tuple[2]),
                'location_id': str(inventory_tuple[3]),
                'quantity': str(inventory_tuple[4]),
                'reserved_quantity': str(inventory_tuple[5]),
                'available_quantity': str(inventory_tuple[6]),
                'damaged_quantity': str(inventory_tuple[7]),
                'created_at': str(inventory_tuple[8]),
                'updated_at': str(inventory_tuple[9])
            }
        except Exception as e:
            print(f"Error converting inventory tuple to dict: {e}")
            print(f"Tuple content: {inventory_tuple}")
            return None

