import sqlite3
import json

conn = sqlite3.connect("./data/database.db")
cursor = conn.cursor()
api_key_list = []
names_list = []
# Query to extract all API keys
try:
    # print("trying")
    cursor.execute("SELECT api_key FROM devices;")
    api_keys = cursor.fetchall()

    # Print all the API keys
    # print("Extracted API Keys:")
    for api_key in api_keys:
        # print(api_key[0])
        api_key_list.append(api_key[0])
    
    
    cursor.execute("SELECT name FROM devices;")
    names = cursor.fetchall()

    # Print all the API keys
    # print("Extracted Names:")
    for name in names:
        # print(api_key[0])
        names_list.append(name[0])

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()

# print(api_key_list)

device_data = [
    {
        "api_key": "____",
        "app": "Device_1_Terminal",
        "endpoint_access": {
            "full": True
        }
    },
    {
        "api_key": "____",
        "app": "Device_1_Computer",
        "endpoint_access": {
            "full": False,
            "warehouses": {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "locations":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "transfers":  {
                "full": True,
            },
            "items":  {
                "full": True,
            },
            "item_lines":  {
                "full": True,
            },
            "item_groups":  {
                "full": True,
            },
            "item_types":  {
                "full": True,
            },
            "suppliers":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "orders":  {
                "full": True,
            },
            "clients":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "shipments":  {
                "full": True,
            }
        }
    },
    {
        "api_key": "____",
        "app": "Device_1_Mobile",
        "endpoint_access": {
            "full": False,
            "warehouses": {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "locations":  {
                "full": False,
                "get": True,
                "post": True,
                "put": True,
                "delete": False
            },
            "transfers":  {
                "full": False,
                "get": True,
                "post": True,
                "put": True,
                "delete": False,
                "commit": True
            },
            "items":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_lines":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_groups":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_types":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "suppliers":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "orders":  {
                "full": False,
                "get": True,
                "post": True,
                "put": True,
                "delete": False
            },
            "clients":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "shipments":  {
                "full": False,
                "get": True,
                "post": True,
                "put": True,
                "delete": False,
                "commit": True
            }
        }
    },
    {
        "api_key": "____",
        "app": "Device_1_Scanner_1",
        "endpoint_access": {
            "full": False,
            "warehouses": {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "locations":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "transfers":  {
                "full": False,
                "get": True,
                "post": True,
                "put": False,
                "delete": False,
                "commit": True
            },
            "items":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_lines":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_groups":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_types":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "suppliers":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "orders":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "clients":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "shipments":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False,
                "commit": False
            }
        }
    },
    {
        "api_key": "____",
        "app": "Device_1_Scanner_2",
        "endpoint_access": {
            "full": False,
            "warehouses": {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "locations":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "transfers":  {
                "full": False,
                "get": True,
                "post": True,
                "put": False,
                "delete": False,
                "commit": True
            },
            "items":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_lines":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_groups":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_types":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "suppliers":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "orders":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "clients":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False
            },
            "shipments":  {
                "full": False,
                "get": False,
                "post": False,
                "put": False,
                "delete": False,
                "commit": False
            }
        }
    },
]

while len(device_data) <= 294:
    # print(len(device_data))
    new_device = device_data[(len(device_data)%5)].copy()
    new_device["api_key"] = api_key_list[len(device_data)-5]
    # print(len(device_data))
    new_device["app"] = names_list[len(device_data)-5]
    # print(new_device["api_key"], new_device["app"])
    # print("\n\n\n")
    # print(new_device)
    # print("\n\n\n")
    device_data.append(new_device)

for device in device_data:
    print(device["api_key"], device["app"])


# with open('transfer_data\device_data.json', 'w') as f:
#     print("dumping")
#     f.write(json.dumps(device_data, indent=4))
