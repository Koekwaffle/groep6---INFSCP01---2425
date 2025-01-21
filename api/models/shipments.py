from api.models.base import Base
from api.providers import data_provider

class Shipments(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def _convert_to_dict(self, row):
        """Convert a database row tuple to a dictionary."""
        if not row:
            return None
        return {
            'id': row[0],
            'order_id': row[1],
            'source_id': row[2],
            'order_date': row[3],
            'request_date': row[4],
            'shipment_date': row[5],
            'shipment_type': row[6],
            'shipment_status': row[7],
            'notes': row[8],
            'carrier_code': row[9],
            'carrier_description': row[10],
            'service_code': row[11],
            'payment_type': row[12],
            'transfer_mode': row[13],
            'total_package_count': row[14],
            'total_package_weight': row[15],
            'created_at': row[16],
            'updated_at': row[17]
        }

    def get_all(self):
        """Retrieve all shipments."""
        query = "SELECT * FROM shipments"
        rows = self.fetch_all(query)
        return [self._convert_to_dict(row) for row in rows] if rows else []

    def get(self, shipment_id):
        """Retrieve a single shipment by ID."""
        query = "SELECT * FROM shipments WHERE id = ?"
        row = self.fetch_one(query, (shipment_id,))
        return self._convert_to_dict(row) if row else None

    def get_items_in_shipment(self, shipment_id):
        """Retrieve all items in a specific shipment."""
        try:
            query = """
            SELECT si.item_id, si.amount, i.code, i.description 
            FROM shipment_items si
            LEFT JOIN items i ON si.item_id = i.uid
            WHERE si.shipment_id = ?
            """
            return self.fetch_all(query, (shipment_id,))
        except Exception as e:
            print(f"Database error in get_items_in_shipment: {str(e)}")
            return None

    def add(self, shipment):
        """Add a new shipment."""
        query = """
        INSERT INTO shipments (order_id, source_id, order_date, request_date, shipment_date, shipment_type, shipment_status, notes, carrier_code, carrier_description, service_code, payment_type, transfer_mode, total_package_count, total_package_weight, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            shipment['order_id'],
            shipment['source_id'],
            shipment['order_date'],
            shipment['request_date'],
            shipment['shipment_date'],
            shipment['shipment_type'],
            shipment['shipment_status'],
            shipment['notes'],
            shipment['carrier_code'],
            shipment['carrier_description'],
            shipment['service_code'],
            shipment['payment_type'],
            shipment['transfer_mode'],
            shipment['total_package_count'],
            shipment['total_package_weight'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, shipment_id, shipment):
        """Update an existing shipment."""
        query = """
        UPDATE shipments
        SET order_id = ?, source_id = ?, order_date = ?, request_date = ?, shipment_date = ?, shipment_type = ?, shipment_status = ?, notes = ?, carrier_code = ?, carrier_description = ?, service_code = ?, payment_type = ?, transfer_mode = ?, total_package_count = ?, total_package_weight = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            shipment['order_id'],
            shipment['source_id'],
            shipment['order_date'],
            shipment['request_date'],
            shipment['shipment_date'],
            shipment['shipment_type'],
            shipment['shipment_status'],
            shipment['notes'],
            shipment['carrier_code'],
            shipment['carrier_description'],
            shipment['service_code'],
            shipment['payment_type'],
            shipment['transfer_mode'],
            shipment['total_package_count'],
            shipment['total_package_weight'],
            self.get_timestamp(),
            shipment_id
        )
        self.execute_query(query, params)

    def remove(self, shipment_id):
        """Remove a shipment by ID."""
        query = "DELETE FROM shipments WHERE id = ?"
        self.execute_query(query, (shipment_id,))

    def get_orders_in_shipment(self, shipment_id):
        """Retrieve all orders for a specific shipment."""
        query = "SELECT id FROM orders WHERE shipment_id = ?"
        return [row[0] for row in self.fetch_all(query, (shipment_id,))]

    def update_orders_in_shipment(self, shipment_id, orders):
        """Update orders associated with a shipment."""
        try:
            # Begin transaction
            self.cursor.execute("BEGIN TRANSACTION")
            
            # Clear existing orders
            query = "UPDATE orders SET shipment_id = NULL WHERE shipment_id = ?"
            self.execute_query(query, (shipment_id,))
            
            # Add new orders
            for order_id in orders:
                query = "UPDATE orders SET shipment_id = ? WHERE id = ?"
                self.execute_query(query, (shipment_id, order_id))
            
            # Update shipment's updated_at timestamp
            query = "UPDATE shipments SET updated_at = ? WHERE id = ?"
            self.execute_query(query, (self.get_timestamp(), shipment_id))
            
            # Commit transaction
            self.cursor.execute("COMMIT")
            return True
        except Exception as e:
            # Rollback on error
            self.cursor.execute("ROLLBACK")
            print(f"Error updating orders in shipment: {e}")
            return False

    def update_items_in_shipment(self, shipment_id, items):
        """Update items associated with a shipment."""
        try:
            # Begin transaction
            self.conn.execute("BEGIN")
            
            # Clear existing items
            query = "DELETE FROM shipment_items WHERE shipment_id = ?"
            self.execute_query(query, (shipment_id,))
            
            # Add new items
            for item in items:
                if isinstance(item, dict) and 'item_id' in item and 'amount' in item:
                    query = """
                    INSERT INTO shipment_items (shipment_id, item_id, amount) 
                    VALUES (?, ?, ?)
                    """
                    self.execute_query(query, (shipment_id, item['item_id'], item['amount']))
            
            # Update shipment's updated_at timestamp
            query = "UPDATE shipments SET updated_at = ? WHERE id = ?"
            self.execute_query(query, (self.get_timestamp(), shipment_id))
            
            # Commit transaction
            self.conn.commit()
            return True
        except Exception as e:
            # Rollback on error
            self.conn.rollback()
            print(f"Error updating items in shipment: {e}")
            return False
