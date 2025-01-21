from api.models.base import Base
from api.providers import data_provider
#It is done
class Clients(Base):
    def __init__(self):
        super().__init__()
        self.conn = data_provider.get_connection()
        self.cursor = self.conn.cursor()

    def get_all(self):
        """Retrieve all clients."""
        query = "SELECT * FROM clients"
        rows = self.fetch_all(query)
        return [self.format_client(row) for row in rows]

    def get(self, client_id):
        """Retrieve a single client by ID."""
        query = "SELECT * FROM clients WHERE id = ?"
        row = self.fetch_one(query, (client_id,))
        return self.format_client(row) if row else None

    def add(self, client):
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

    def update(self, client_id, client):
        """Update an existing client."""
        query = """
        UPDATE clients
        SET name = ?, address = ?, city = ?, zip_code = ?, province = ?, country = ?, contact_name = ?, contact_phone = ?, contact_email = ?, updated_at = ?
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

    def remove(self, client_id):
        """Remove a client by ID."""
        query = "DELETE FROM clients WHERE id = ?"
        self.execute_query(query, (client_id,))

    def format_client(self, row):
        """Format a client row into a dictionary."""
        return {
            'id': row[0],
            'name': row[1],
            'address': row[2],
            'city': row[3],
            'zip_code': row[4],
            'province': row[5],
            'country': row[6],
            'contact_name': row[7],
            'contact_phone': row[8],
            'contact_email': row[9],
            'created_at': row[10],
            'updated_at': row[11]
        }
