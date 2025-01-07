
from api.models.base import Base

class Clients(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all clients."""
        query = "SELECT * FROM clients"
        return self.fetch_all(query)

    def get(self, client_id):
        """Retrieve a single client by ID."""
        query = "SELECT * FROM clients WHERE id = ?"
        return self.fetch_one(query, (client_id,))

    def create(self, client):
        """Add a new client."""
        query = "INSERT INTO clients (name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        return self.execute_query(query, (client['name'], client['address'], client['city'], client['zip_code'], client['province'], client['country'], client['contact_name'], client['contact_phone'], client['contact_email']))

    def update(self, client_id, client):
        """Update an existing client."""
        query = "UPDATE clients SET name = ?, address = ?, city = ?, zip_code = ?, province = ?, country = ?, contact_name = ?, contact_phone = ?, contact_email = ? WHERE id = ?"
        return self.execute_query(query, (client['name'], client['address'], client['city'], client['zip_code'], client['province'], client['country'], client['contact_name'], client['contact_phone'], client['contact_email'], client_id))

    def delete(self, client_id):
        """Delete a client by ID."""
        query = "DELETE FROM clients WHERE id = ?"
        return self.execute_query(query, (client_id,))
