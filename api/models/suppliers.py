from api.models.base import Base
from api.providers import data_provider

class Suppliers(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all suppliers."""
        query = "SELECT * FROM suppliers"
        return self.fetch_all(query)

    def get(self, supplier_id):
        """Retrieve a single supplier by ID."""
        query = "SELECT * FROM suppliers WHERE id = ?"
        return self.fetch_one(query, (supplier_id,))

    def add(self, supplier):
        """Add a new supplier."""
        query = """
        INSERT INTO suppliers (name, contact_name, contact_email, contact_phone, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            supplier['name'],
            supplier['contact_name'],
            supplier['contact_email'],
            supplier['contact_phone'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, supplier_id, supplier):
        """Update an existing supplier."""
        query = """
        UPDATE suppliers
        SET name = ?, contact_name = ?, contact_email = ?, contact_phone = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            supplier['name'],
            supplier['contact_name'],
            supplier['contact_email'],
            supplier['contact_phone'],
            self.get_timestamp(),
            supplier_id
        )
        self.execute_query(query, params)

    def remove(self, supplier_id):
        """Remove a supplier by ID."""
        query = "DELETE FROM suppliers WHERE id = ?"
        self.execute_query(query, (supplier_id,))

    def get_items_for_supplier(self, supplier_id):
        query = "SELECT * FROM items WHERE supplier_id = ?"
        return self.fetch_all(query, (supplier_id,))
