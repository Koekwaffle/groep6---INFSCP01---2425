from api.models.base import Base

class Warehouses(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all warehouses."""
        query = "SELECT * FROM warehouses"
        return self.fetch_all(query)

    def get(self, warehouse_id):
        """Retrieve a single warehouse by ID."""
        query = "SELECT * FROM warehouses WHERE id = ?"
        return self.fetch_one(query, (warehouse_id,))

    def add_warehouse(self, warehouse):
        """Add a new warehouse."""
        query = """
        INSERT INTO warehouses (name, location, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            warehouse['name'],
            warehouse['location'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_warehouse(self, warehouse_id, warehouse):
        """Update an existing warehouse."""
        query = """
        UPDATE warehouses
        SET name = ?, location = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            warehouse['name'],
            warehouse['location'],
            self.get_timestamp(),
            warehouse_id
        )
        self.execute_query(query, params)

    def remove_warehouse(self, warehouse_id):
        """Remove a warehouse by ID."""
        query = "DELETE FROM warehouses WHERE id = ?"
        self.execute_query(query, (warehouse_id,))