from api.models.base import Base
from api.providers import data_provider

class Shipments(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all shipments."""
        query = "SELECT * FROM shipments"
        return self.fetch_all(query)

    def get(self, shipment_id):
        """Retrieve a single shipment by ID."""
        query = "SELECT * FROM shipments WHERE id = ?"
        return self.fetch_one(query, (shipment_id,))

    def get_items_in_shipment(self, shipment_id):
        """Retrieve all items in a specific shipment."""
        query = "SELECT * FROM shipment_items WHERE shipment_id = ?"
        return self.fetch_all(query, (shipment_id,))

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
