from api.models.base import Base

class Transfers(Base):
    def __init__(self):
        super().__init__()

    def gets(self):
        """Retrieve all transfers."""
        query = "SELECT * FROM transfers"
        return self.fetch_all(query)

    def get_transfer(self, transfer_id):
        """Retrieve a single transfer by ID."""
        query = "SELECT * FROM transfers WHERE id = ?"
        return self.fetch_one(query, (transfer_id,))

    def get_items_in_transfer(self, transfer_id):
        """Retrieve all items in a specific transfer."""
        query = "SELECT * FROM transfer_items WHERE transfer_id = ?"
        return self.fetch_all(query, (transfer_id,))

    def add_transfer(self, transfer):
        """Add a new transfer."""
        query = """
        INSERT INTO transfers (name, transfer_status, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            transfer['name'],
            "Scheduled",
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_transfer(self, transfer_id, transfer):
        """Update an existing transfer."""
        query = """
        UPDATE transfers
        SET name = ?, transfer_status = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            transfer['name'],
            transfer['transfer_status'],
            self.get_timestamp(),
            transfer_id
        )
        self.execute_query(query, params)

    def remove_transfer(self, transfer_id):
        """Remove a transfer by ID."""
        query = "DELETE FROM transfers WHERE id = ?"
        self.execute_query(query, (transfer_id,))
