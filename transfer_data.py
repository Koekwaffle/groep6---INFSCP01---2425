import sqlite3
import json
from data.dbconn import get_db_connection  # Import the connection function

# Connect to your SQLite database
conn = get_db_connection()  
cursor = conn.cursor()

# Verify the connection by checking existing tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Existing tables:", cursor.fetchall())

# Function to insert data into locations table
def insert_location(location):
    query = '''
    INSERT INTO locations 
    (id, warehouse_id, code, name, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    data = (
        location['id'], 
        location['warehouse_id'], 
        location['code'], 
        location['name'], 
        location['created_at'], 
        location['updated_at']
    )
    cursor.execute(query, data)

# Load the locations JSON data
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\locations.json', 'r') as file:
    locations = json.load(file)

# Insert each location into the locations table
for location in locations:
    insert_location(location)

# Commit the transaction and close the connection
conn.commit()
conn.close()
