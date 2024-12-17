from api.models.base import Base

class Suppliers(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all suppliers."""
        query = "SELECT * FROM suppliers"
        return self.fetch_all(query)

    def get(self, supplier_id):
        """Retrieve a single supplier by ID."""
        query = "SELECT * FROM suppliers WHERE id = ?"
        return self.fetch_one(query, (supplier_id,))

    def add_supplier(self, supplier):
        """Add a new supplier."""
        query = """
        INSERT INTO suppliers (name, address, contact, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            supplier['name'],
            supplier['address'],
            supplier['contact'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_supplier(self, supplier_id, supplier):
        """Update an existing supplier."""
        query = """
        UPDATE suppliers
        SET name = ?, address = ?, contact = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            supplier['name'],
            supplier['address'],
            supplier['contact'],
            self.get_timestamp(),
            supplier_id
        )
        self.execute_query(query, params)

    def remove_supplier(self, supplier_id):
        """Remove a supplier by ID."""
        query = "DELETE FROM suppliers WHERE id = ?"
        self.execute_query(query, (supplier_id,))
