from api.models.base import Base
from api.providers import data_provider

class Warehouses(Base):
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
            'code': row[1],
            'name': row[2],
            'address': row[3],
            'city': row[4],
            'province': row[5],
            'country': row[6],
            'created_at': row[7],
            'updated_at': row[8]
        }

    def get_all(self):
        print("\n\n\nGetting all warehouses...\n\n\n")
        """Retrieve all warehouses."""
        query = "SELECT * FROM warehouses"
        rows = self.fetch_all(query)
        return [self._convert_to_dict(row) for row in rows] if rows else []

    def get(self, warehouse_id):
        print("\n\n\nGetting warehouse by ID...\n\n\n")
        """Retrieve a single warehouse by ID."""
        query = "SELECT * FROM warehouses WHERE id = ?"
        row = self.fetch_one(query, (warehouse_id,))
        return self._convert_to_dict(row) if row else None

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

    def get_warehouse_locations(self, warehouse_id):
        """Retrieve all locations for a warehouse."""
        query = "SELECT * FROM locations WHERE warehouse_id = ?"
        rows = self.fetch_all(query, (warehouse_id,))
        from CargoHubApp.models import Location
        location_fields = ["id", "warehouse_id", "name"]
        location_objects = []
        for row in rows:
            data = dict(zip(location_fields, row))
            location_objects.append(Location(**data))
        return location_objects