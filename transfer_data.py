import sqlite3
import json
from data.dbconn import get_db_connection

def insert_shipment(shipment):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the shipment already exists to avoid duplicates
    cursor.execute("SELECT id FROM shipments WHERE id = ?", (shipment['id'],))
    existing_shipment = cursor.fetchone()
    
    if existing_shipment:
        print(f"Shipment ID {shipment['id']} already exists. Skipping insertion.")
        return  # Skip if it already exists

    query = '''
    INSERT INTO shipments 
    (id, order_id, source_id, order_date, request_date, shipment_date, shipment_type, 
    shipment_status, notes, carrier_code, carrier_description, service_code, payment_type, 
    transfer_mode, total_package_count, total_package_weight, created_at, updated_at) 
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
        shipment.get('notes', ''),
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
    conn.commit()
    conn.close()

def insert_shipment_items(shipment_id, items):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert each item associated with the shipment
    for item in items:
        item_id = item["item_id"]
        amount = item["amount"]
        
        cursor.execute('''
            INSERT INTO shipment_items (shipment_id, item_id, amount)
            VALUES (?, ?, ?)
        ''', (shipment_id, item_id, amount))
    
    conn.commit()
    conn.close()

# Load the shipments JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\shipments.json', 'r') as file:
    shipments = json.load(file)

# Insert each shipment and its items
for shipment in shipments:
    insert_shipment(shipment)  # Insert the shipment into the shipments table
    insert_shipment_items(shipment['id'], shipment['items'])  # Insert items into the shipment_items table

print("All shipments and shipment items have been inserted into the database.")
