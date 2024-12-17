from api.models.base import Base

class Shipments(Base):
    def __init__(self):
        super().__init__()

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

    def add_shipment(self, shipment):
        """Add a new shipment."""
        query = """
        INSERT INTO shipments (name, created_at, updated_at)
        VALUES (?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            shipment['name'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_shipment(self, shipment_id, shipment):
        """Update an existing shipment."""
        query = """
        UPDATE shipments
        SET name = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            shipment['name'],
            self.get_timestamp(),
            shipment_id
        )
        self.execute_query(query, params)

    def remove_shipment(self, shipment_id):
        """Remove a shipment by ID."""
        query = "DELETE FROM shipments WHERE id = ?"
        self.execute_query(query, (shipment_id,))
