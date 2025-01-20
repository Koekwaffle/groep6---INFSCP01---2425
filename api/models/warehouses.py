from api.models.base import Base
from api.providers import data_provider

class Warehouses(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all warehouses."""
        query = "SELECT * FROM warehouses"
        return self.fetch_all(query)

    def get(self, warehouse_id):
        """Retrieve a single warehouse by ID."""
        query = "SELECT * FROM warehouses WHERE id = ?"
        return self.fetch_one(query, (warehouse_id,))

    def add(self, warehouse):
        """Add a new warehouse."""
        query = """
        INSERT INTO warehouses (code, name, address, city, province, country, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            warehouse['code'],
            warehouse['name'],
            warehouse['address'],
            warehouse.get('city', ''),
            warehouse['province'],
            warehouse['country'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, warehouse_id, warehouse):
        """Update an existing warehouse."""
        query = """
        UPDATE warehouses
        SET code = ?, name = ?, address = ?, city = ?, province = ?, country = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            warehouse.get('code', ''),  # Ensure 'code' key exists
            warehouse['name'],
            warehouse['address'],
            warehouse.get('city', ''),
            warehouse['province'],
            warehouse['country'],
            self.get_timestamp(),
            warehouse_id
        )
        self.execute_query(query, params)

    def remove(self, warehouse_id):
        """Remove a warehouse by ID."""
        query = "DELETE FROM warehouses WHERE id = ?"
        self.execute_query(query, (warehouse_id,))