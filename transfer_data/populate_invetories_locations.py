import sqlite3
import json
from data.dbconn import get_db_connection  # Ensure this path is correct

def insert_inventory_location(inventory_id, location_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO inventory_locations (inventory_id, location_id)
    VALUES (?, ?)
    '''
    cursor.execute(query, (inventory_id, location_id))
    conn.commit()
    conn.close()

# Step 1: Load locations.json to confirm valid location IDs
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\locations.json', 'r') as loc_file:
    locations = json.load(loc_file)
    valid_location_ids = {loc['id'] for loc in locations}  # Set of valid location IDs

# Step 2: Load inventories.json
with open('C:\\Users\\ronan\\Documents\\GitHub\\groep6---INFSCP01---2425\\data\\inventories.json', 'r') as inv_file:
    inventories = json.load(inv_file)

# Step 3: Insert each inventory's locations into the inventory_locations table
for inventory in inventories:
    inventory_id = inventory['id']
    location_ids = inventory['locations']  # List of location IDs from inventories.json

    # Insert each location_id directly if it's valid
    for location_id in location_ids:
        if location_id in valid_location_ids:
            insert_inventory_location(inventory_id, location_id)
        else:
            print(f"Location ID {location_id} not found in locations table.")

print("All inventory locations have been inserted into the inventory_locations table using location IDs.")
