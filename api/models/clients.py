import sqlite3
from api.models.base import Base
from api.models.Database_file import db_start

class Clients(Base):
    def __init__(self):
        self.dbfile = "database.db"
        self.db = db_start()

    def gets(self):
        conn = self.db.connection(self.dbfile)
        if conn is None:
            print("DB connection failed")
            return None  # If connection fails, return None
        cursor = conn.cursor()

        query = "SELECT * FROM clients LIMIT 10"
        cursor.execute(query)
        clients = cursor.fetchall()  # Fetch rows
        
        if not clients:
            print("No clients found")
            return None
        
        # Return clients as a list of dictionaries
        clients_list = []
        for client in clients:
            clients_list.append({
                'id': client[0],
                'name': client[1],
                'address': client[2],
                'city': client[3],
                'zip_code': client[4],
                'province': client[5],
                'country': client[6],
                'contact_name': client[7],
                'contact_phone': client[8],
                'contact_email': client[9],
                'created_at': client[10],
                'updated_at': client[11],
            })
        
        cursor.close()
        conn.close()
        return clients_list

    def get(self, client_id):
        conn = self.db.connection(self.dbfile)
        if conn is None:
            print("DB connection failed")
            return None  # If connection fails, return None
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM clients WHERE id = ?"
            cursor.execute(query, (client_id,))  # Pass the client_id as a tuple
            client = cursor.fetchone()  # Fetch a single row
            
            if client is None:
                print(f"No client with id {client_id}")
                return None

            return {
                'id': client[0],
                'name': client[1],
                'address': client[2],
                'city': client[3],
                'zip_code': client[4],
                'province': client[5],
                'country': client[6],
                'contact_name': client[7],
                'contact_phone': client[8],
                'contact_email': client[9],
                'created_at': client[10],
                'updated_at': client[11],
            }

        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
            return None

        finally:
            cursor.close()
            conn.close()
        
    def add(self, client):
        conn = self.db.connection(self.dbfile)
        if conn is None:
            print("DB connection failed")
            return None  # If connection fails, return None
        cursor = conn.cursor()

        client["created_at"] = self.get_timestamp()
        client["updated_at"] = self.get_timestamp()
        
        query = f"""INSERT INTO clients (
            id, name, address, city, zip_code, province, country, 
            contact_name, contact_phone, contact_email, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        
        data = (
            client['id'], 
            client['name'], 
            client['address'], 
            client['city'], 
            client['zip_code'], 
            client['province'], 
            client['country'], 
            client['contact_name'], 
            client['contact_phone'], 
            client['contact_email'], 
            client['created_at'],
            client['updated_at'])
        
        cursor.execute(query, data)
        conn.commit()

        print(f"Client {client['name']} added successfully.")

        cursor.close()
        conn.close()

    def update(self, client_id, client):
        # Establish connection to the database
        conn = self.db.connection(self.dbfile)
        if conn is None:
            print("DB connection failed")
            return None  # Exit if connection fails
        
        try:
            cursor = conn.cursor()

            # Check if the client exists
            cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
            client_old = cursor.fetchone()
            if client_old is None:
                print("Client not found")
                return None

            # Define the update query with placeholders
            update_query = """
                UPDATE clients SET
                    name = ?,
                    address = ?,
                    city = ?,
                    zip_code = ?,
                    province = ?,
                    country = ?,
                    contact_name = ?,
                    contact_phone = ?,
                    contact_email = ?,
                    created_at = ?,
                    updated_at = ?
                WHERE id = ?
            """

            # Execute the update query
            cursor.execute(update_query, (
                client['name'],
                client['address'],
                client['city'],
                client['zip_code'],
                client['province'],
                client['country'],
                client['contact_name'],
                client['contact_phone'],
                client['contact_email'],
                client['created_at'],
                self.get_timestamp(),  # Assuming this method returns the current timestamp
                client_id
            ))

            # Commit the changes to the database
            conn.commit()
            print("Client updated successfully.")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()  # Rollback if any error occurs
        finally:
            cursor.close()
            conn.close()

    def remove(self, client_id):
        conn = self.db.connection(self.dbfile)
        if conn is None:
            print("DB connection failed")
            return None  # If connection fails, return None
        cursor = conn.cursor()

        query = f"DELETE FROM clients WHERE id = {client_id}"
        cursor.execute(query)

        conn.commit()
        cursor.close()
        conn.close()
