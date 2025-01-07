from api.models.base import Base

class Clients(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        """Retrieve all clients."""
        query = "SELECT * FROM clients"
        results = self.fetch_all(query)
        clients = []
        for result in results:
            clients.append({
                "id": result[0],
                "name": result[1],
                "address": result[2],
                "city": result[3],
                "zip_code": result[4],
                "province": result[5],
                "country": result[6],
                "contact_name": result[7],
                "contact_phone": result[8],
                "contact_email": result[9],
                "created_at": result[10],
                "updated_at": result[11],
            })
        return clients

    def get(self, client_id):
        """Retrieve a single client by ID."""
        query = "SELECT * FROM clients WHERE id = ?"
        result = self.fetch_one(query, (client_id,))
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "address": result[2],
                "city": result[3],
                "zip_code": result[4],
                "province": result[5],
                "country": result[6],
                "contact_name": result[7],
                "contact_phone": result[8],
                "contact_email": result[9],
                "created_at": result[10],
                "updated_at": result[11],
            }
        return None

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

    def remove(self, client_id):
        """Remove a client by ID."""
        query = "DELETE FROM clients WHERE id = ?"
        self.execute_query(query, (client_id,))
