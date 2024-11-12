import sqlite3
import json
from data.dbconn import get_db_connection  # Ensure this path is correct

# Function to insert warehouse data into the warehouses table
def insert_warehouse(warehouse):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the warehouse already exists to avoid duplicates
    cursor.execute("SELECT id FROM warehouses WHERE id = ?", (warehouse['id'],))
    existing_warehouse = cursor.fetchone()
    
    if existing_warehouse:
        print(f"Warehouse ID {warehouse['id']} already exists. Skipping insertion.")
        return  # Skip if it already exists

    query = '''
    INSERT INTO warehouses 
    (id, code, name, address, zip, city, province, country, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    data = (
        warehouse['id'],
        warehouse['code'],
        warehouse['name'],
        warehouse['address'],
        warehouse['zip'],
        warehouse['city'],
        warehouse['province'],
        warehouse['country'],
        warehouse['created_at'],
        warehouse['updated_at']
    )
    cursor.execute(query, data)
    conn.commit()
    conn.close()

# Function to insert contact data into the contacts table, linked to a warehouse
def insert_contact(warehouse_id, contact):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO contacts 
    (warehouse_id, name, phone, email, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    data = (
        warehouse_id,
        contact['name'],
        contact['phone'],
        contact['email'],
        None,  # Set created_at if needed (or use a default value)
        None   # Set updated_at if needed (or use a default value)
    )
    cursor.execute(query, data)
    conn.commit()
    conn.close()

# Load the warehouses JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\warehouses.json', 'r') as file:
    warehouses = json.load(file)

# Insert each warehouse and its contact into their respective tables
for warehouse in warehouses:
    insert_warehouse(warehouse)  # Insert the warehouse into the warehouses table
    insert_contact(warehouse['id'], warehouse['contact'])  # Insert the contact into the contacts table

print("All warehouses and contacts have been inserted into their respective tables.")
