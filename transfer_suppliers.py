import sqlite3
import json
from data.dbconn import get_db_connection  # Ensure this path is correct

def insert_supplier(supplier):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the supplier already exists to avoid duplicates
    cursor.execute("SELECT id FROM suppliers WHERE id = ?", (supplier['id'],))
    existing_supplier = cursor.fetchone()
    
    if existing_supplier:
        print(f"Supplier ID {supplier['id']} already exists. Skipping insertion.")
        return  # Skip if it already exists

    query = '''
    INSERT INTO suppliers 
    (id, code, name, address, address_extra, city, zip_code, province, country, 
    contact_name, phonenumber, reference, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    data = (
        supplier['id'], 
        supplier['code'], 
        supplier['name'], 
        supplier['address'], 
        supplier.get('address_extra', ''),  # Default to empty if missing
        supplier['city'], 
        supplier['zip_code'], 
        supplier['province'], 
        supplier['country'], 
        supplier['contact_name'], 
        supplier['phonenumber'], 
        supplier['reference'], 
        supplier['created_at'], 
        supplier['updated_at']
    )
    cursor.execute(query, data)
    conn.commit()
    conn.close()

# Load the suppliers JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\suppliers.json', 'r') as file:
    suppliers = json.load(file)

# Insert each supplier into the suppliers table
for supplier in suppliers:
    insert_supplier(supplier)

print("All suppliers have been inserted into the suppliers table.")
