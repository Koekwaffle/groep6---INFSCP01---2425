import sqlite3
import random
import string
from datetime import datetime
from dbconn import get_db_connection
# Function to generate a random API key
def generate_api_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) 

# Connect to the database
conn = sqlite3.connect(get_db_connection())
cursor = conn.cursor()

# Define the range of warehouses and number of devices per warehouse
warehouses = range(1, 59)
devices_per_warehouse = 5

# Current timestamp for created_at and updated_at
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prepare data for insertion
device_data = []
for warehouse_id in warehouses:
    for device_num in range(1, devices_per_warehouse + 1):
        device_name = f"Device_{warehouse_id}_{device_num}"
        api_key = generate_api_key()
        device_data.append((device_name, warehouse_id, api_key, '', current_timestamp, current_timestamp))

# Insert data into the devices table
try:
    cursor.executemany("""
        INSERT INTO devices (name, warehouse_id, api_key, permissions, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?);
    """, device_data)
    conn.commit()
    print(f"Inserted {len(device_data)} devices successfully!")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
