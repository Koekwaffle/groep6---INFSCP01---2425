from api.models.base import Base

class Locations(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all locations."""
        query = "SELECT * FROM locations"
        return self.fetch_all(query)

    def get(self, location_id):
        """Retrieve a single location by ID."""
        query = "SELECT * FROM locations WHERE id = ?"
        return self.fetch_one(query, (location_id,))

    def get_locations_in_warehouse(self, warehouse_id):
        """Retrieve all locations in a specific warehouse."""
        query = "SELECT * FROM locations WHERE warehouse_id = ?"
        return self.fetch_all(query, (warehouse_id,))

    def add_location(self, location):
        """Add a new location."""
        query = """
        INSERT INTO locations (name, warehouse_id, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            location['name'],
            location['warehouse_id'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_location(self, location_id, location):
        """Update an existing location."""
        query = """
        UPDATE locations
        SET name = ?, warehouse_id = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            location['name'],
            location['warehouse_id'],
            self.get_timestamp(),
            location_id
        )
        self.execute_query(query, params)

    def remove_location(self, location_id):
        """Remove a location by ID."""
        query = "DELETE FROM locations WHERE id = ?"
        self.execute_query(query, (location_id,))
