from api.models.base import Base
from api.providers import data_provider

class Items(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all items."""
        query = "SELECT * FROM items"
        return self.fetch_all(query)

    def get(self, item_uid):
        """Retrieve a single item by UID."""
        query = "SELECT * FROM items WHERE uid = ?"
        return self.fetch_one(query, (item_uid,))

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

    def add(self, item):
        """Add a new item."""
        query = """
        INSERT INTO items (uid, code, description, short_description, upc_code, model_number, commodity_code, item_line, item_group, item_type, unit_purchase_quantity, unit_order_quantity, pack_order_quantity, supplier_id, supplier_code, supplier_part_number, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            item['uid'],
            item['code'],
            item['description'],
            item['short_description'],
            item['upc_code'],
            item['model_number'],
            item['commodity_code'],
            item['item_line'],
            item['item_group'],
            item['item_type'],
            item['unit_purchase_quantity'],
            item['unit_order_quantity'],
            item['pack_order_quantity'],
            item['supplier_id'],
            item['supplier_code'],
            item['supplier_part_number'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, item_uid, item):
        """Update an existing item."""
        query = """
        UPDATE items
        SET uid = ?, code = ?, description = ?, short_description = ?, upc_code = ?, model_number = ?, commodity_code = ?, item_line = ?, item_group = ?, item_type = ?, unit_purchase_quantity = ?, unit_order_quantity = ?, pack_order_quantity = ?, supplier_id = ?, supplier_code = ?, supplier_part_number = ?, updated_at = ?
        WHERE uid = ?
        """
        params = (
            item['uid'],
            item['code'],
            item['description'],
            item['short_description'],
            item['upc_code'],
            item['model_number'],
            item['commodity_code'],
            item['item_line'],
            item['item_group'],
            item['item_type'],
            item['unit_purchase_quantity'],
            item['unit_order_quantity'],
            item['pack_order_quantity'],
            item['supplier_id'],
            item['supplier_code'],
            item['supplier_part_number'],
            self.get_timestamp(),
            item_uid
        )
        self.execute_query(query, params)

    def remove(self, item_uid):
        """Remove an item by UID."""
        query = "DELETE FROM items WHERE uid = ?"
        self.execute_query(query, (item_uid,))

    def tuple_to_dict(self, item_tuple):
        """Convert a tuple to a dictionary with named fields"""
        try:
            return {
                'uid': str(item_tuple[0]) if item_tuple[0] is not None else None,
                'code': str(item_tuple[1]) if item_tuple[1] is not None else None,
                'description': str(item_tuple[2]) if item_tuple[2] is not None else None,
                'short_description': str(item_tuple[3]) if item_tuple[3] is not None else None,
                'upc_code': str(item_tuple[4]) if item_tuple[4] is not None else None,
                'model_number': str(item_tuple[5]) if item_tuple[5] is not None else None,
                'commodity_code': str(item_tuple[6]) if item_tuple[6] is not None else None,
                'item_line': str(item_tuple[7]) if item_tuple[7] is not None else None,  # Changed to str
                'item_group': str(item_tuple[8]) if item_tuple[8] is not None else None,  # Changed to str
                'item_type': str(item_tuple[9]) if item_tuple[9] is not None else None,  # Changed to str
                'unit_purchase_quantity': str(item_tuple[10]) if item_tuple[10] is not None else '0',
                'unit_order_quantity': str(item_tuple[11]) if item_tuple[11] is not None else '0',
                'pack_order_quantity': str(item_tuple[12]) if item_tuple[12] is not None else '0',
                'supplier_id': str(item_tuple[13]) if item_tuple[13] is not None else None,
                'supplier_code': str(item_tuple[14]) if item_tuple[14] is not None else None,
                'supplier_part_number': str(item_tuple[15]) if item_tuple[15] is not None else None,
                'created_at': str(item_tuple[16]) if item_tuple[16] is not None else None,
                'updated_at': str(item_tuple[17]) if item_tuple[17] is not None else None
            }
        except Exception as e:
            print(f"Error converting tuple to dict: {e}")
            print(f"Tuple content: {item_tuple}")
            return None

    def get_by_group(self, group_id):
        """Get all items belonging to a specific item group"""
        try:
            query = """
            SELECT uid, code, description, short_description, upc_code, 
                   model_number, commodity_code, item_line, item_group, item_type,
                   unit_purchase_quantity, unit_order_quantity, pack_order_quantity,
                   supplier_id, supplier_code, supplier_part_number, 
                   created_at, updated_at
            FROM items 
            WHERE item_group = ?
            """
            items = self.fetch_all(query, (int(group_id),))
            if items:
                item_dicts = [self.tuple_to_dict(item) for item in items]
                # Filter out None values in case any conversion failed
                return [item for item in item_dicts if item is not None]
            return None
        except Exception as e:
            print(f"Error getting items by group: {e}")
            return None
