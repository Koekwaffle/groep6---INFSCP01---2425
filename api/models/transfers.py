from api.models.base import Base
from api.providers import data_provider

class Transfers(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all transfers."""
        query = "SELECT * FROM transfers"
        return self.fetch_all(query)

    def get(self, transfer_id):
        """Retrieve a single transfer by ID."""
        query = "SELECT * FROM transfers WHERE id = ?"
        return self.fetch_one(query, (transfer_id,))

    def get_items_in_transfer(self, transfer_id):
        """Retrieve all items in a specific transfer."""
        query = "SELECT * FROM transfer_items WHERE transfer_id = ?"
        return self.fetch_all(query, (transfer_id,))

    def add(self, transfer):
        """Add a new transfer."""
        query = """
        INSERT INTO transfers (transfer_status, created_at, updated_at)
        VALUES (?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            "Scheduled",
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update(self, transfer_id, transfer):
        """Update an existing transfer."""
        query = """
        UPDATE transfers
        SET transfer_status = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            transfer['transfer_status'],
            self.get_timestamp(),
            transfer_id
        )
        self.execute_query(query, params)

    def remove(self, transfer_id):
        """Remove a transfer by ID."""
        query = "DELETE FROM transfers WHERE id = ?"
        self.execute_query(query, (transfer_id,))

    def add_item_to_transfer(self, transfer_id, item_id, amount):
        """Add an item to a specific transfer."""
        query = """
        INSERT INTO transfer_items (transfer_id, item_id, amount)
        VALUES (?, ?, ?)
        """
        self.execute_query(query, (transfer_id, item_id, amount))
