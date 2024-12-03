from api.models.base import Base

class Clients(Base):
    def __init__(self):
        super().__init__()

    def gets(self):
        """Retrieve all clients."""
        query = "SELECT * FROM clients"
        return self.fetch_all(query)

    def get_client(self, client_id):
        """Retrieve a single client by ID."""
        query = "SELECT * FROM clients WHERE id = ?"
        return self.fetch_one(query, (client_id,))

    def add_client(self, client):
        """Add a new client."""
        query = """
        INSERT INTO clients (name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            client['name'],
            client['address'],
            client['city'],
            client['zip_code'],
            client['province'],
            client['country'],
            client['contact_name'],
            client['contact_phone'],
            client['contact_email'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_client(self, client_id, client):
        """Update an existing client."""
        query = """
        UPDATE clients
        SET name = ?, address = ?, city = ?, zip_code = ?, province = ?, country = ?,
            contact_name = ?, contact_phone = ?, contact_email = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            client['name'],
            client['address'],
            client['city'],
            client['zip_code'],
            client['province'],
            client['country'],
            client['contact_name'],
            client['contact_phone'],
            client['contact_email'],
            self.get_timestamp(),
            client_id
        )
        self.execute_query(query, params)

    def remove_client(self, client_id):
        """Remove a client by ID."""
        query = "DELETE FROM clients WHERE id = ?"
        self.execute_query(query, (client_id,))
