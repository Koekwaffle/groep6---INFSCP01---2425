import sqlite3
import json
from data.dbconn import get_db_connection  # Import the connection function

# Connect to your SQLite database
conn = get_db_connection()  
cursor = conn.cursor()

# Verify the connection by checking existing tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Existing tables:", cursor.fetchall())

# Function to insert data into shipments table with duplicate check
def insert_shipment(shipment):
    # Check if the shipment already exists
    cursor.execute("SELECT id FROM shipments WHERE id = ?", (shipment['id'],))
    existing_shipment = cursor.fetchone()
    
    if existing_shipment:
        print(f"Shipment ID {shipment['id']} already exists. Skipping insertion.")
        return  # Skip this shipment if it already exists

    query = '''
    INSERT INTO shipments 
    (id, order_id, source_id, order_date, request_date, shipment_date, shipment_type, shipment_status, notes, 
    carrier_code, carrier_description, service_code, payment_type, transfer_mode, total_package_count, 
    total_package_weight, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    data = (
        shipment['id'], 
        shipment['order_id'], 
        shipment['source_id'], 
        shipment['order_date'], 
        shipment['request_date'], 
        shipment['shipment_date'], 
        shipment['shipment_type'], 
        shipment['shipment_status'], 
        shipment.get('notes', ''),  # Use an empty string if notes are missing
        shipment['carrier_code'], 
        shipment['carrier_description'], 
        shipment['service_code'], 
        shipment['payment_type'], 
        shipment['transfer_mode'], 
        shipment['total_package_count'], 
        shipment['total_package_weight'], 
        shipment['created_at'], 
        shipment['updated_at']
    )
    cursor.execute(query, data)

# Load the shipments JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\shipments.json', 'r') as file:
    shipments = json.load(file)

# Insert each shipment into the shipments table
for shipment in shipments:
    insert_shipment(shipment)

# Commit the transaction and close the connection
conn.commit()
conn.close()
