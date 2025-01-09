import sqlite3

# Connect to the database
conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# Query to extract all API keys
try:
    cursor.execute("SELECT api_key FROM devices;")
    api_keys = cursor.fetchall()

    # Print all the API keys
    print("Extracted API Keys:")
    for api_key in api_keys:
        print(api_key[0])

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
