import sqlite3
import json
from data.dbconn import get_db_connection  # Ensure this path is correct

# Function to insert transfer data into the transfers table
def insert_transfer(transfer):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the transfer already exists to avoid duplicates
    cursor.execute("SELECT id FROM transfers WHERE id = ?", (transfer['id'],))
    existing_transfer = cursor.fetchone()
    
    if existing_transfer:
        print(f"Transfer ID {transfer['id']} already exists. Skipping insertion.")
        return  # Skip if it already exists

    query = '''
    INSERT INTO transfers 
    (id, reference, transfer_from, transfer_to, transfer_status, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    data = (
        transfer['id'],
        transfer['reference'],
        transfer['transfer_from'],
        transfer['transfer_to'],
        transfer['transfer_status'],
        transfer['created_at'],
        transfer['updated_at']
    )
    cursor.execute(query, data)
    conn.commit()
    conn.close()

# Function to insert transfer items into the transfer_items table
def insert_transfer_items(transfer_id, items):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert each item associated with the transfer
    for item in items:
        item_id = item["item_id"]
        amount = item["amount"]
        
        cursor.execute('''
            INSERT INTO transfer_items (transfer_id, item_id, amount)
            VALUES (?, ?, ?)
        ''', (transfer_id, item_id, amount))
    
    conn.commit()
    conn.close()

# Load the transfers JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\transfers.json', 'r') as file:
    transfers = json.load(file)

# Insert each transfer and its items
for transfer in transfers:
    insert_transfer(transfer)  # Insert the transfer into the transfers table
    insert_transfer_items(transfer['id'], transfer['items'])  # Insert items into the transfer_items table

print("All transfers and transfer items have been inserted into the database.")
