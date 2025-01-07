import sqlite3
import json
from data.dbconn import get_db_connection  # Import the connection function

# Connect to your SQLite database
conn = get_db_connection()  
cursor = conn.cursor()

# Verify the connection by checking existing tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Existing tables:", cursor.fetchall())

# Function to insert data into clients table
def insert_client(client):
    query = '''
    INSERT INTO clients 
    (id, name, address, city, zip_code, province, country, contact_name, contact_phone, contact_email, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
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
        client.get('created_at'), 
        client.get('updated_at')
    )
    cursor.execute(query, data)

# Load the clients JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\clients.json', 'r') as file:
    clients = json.load(file)

# Insert each client into the clients table
for client in clients:
    insert_client(client)

# Commit the transaction and close the connection
conn.commit()
conn.close()
