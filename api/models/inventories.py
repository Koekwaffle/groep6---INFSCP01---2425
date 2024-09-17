
import json

from models.base import Base  # Assuming that Base class provides common functionalities like timestamps

# Global list used to store inventories if 'is_debug' mode is enabled
INVENTORIES = []


class Inventories(Base):
    def __init__(self, root_path, is_debug=False):
        # Set the path to the inventories.json file based on the provided root_path
        self.data_path = root_path + "inventories.json"
        # Load data from file or use debug data
        self.load(is_debug)

    # Returns all inventory data
    def get_inventories(self):
        return self.data

    # Retrieves a specific inventory entry by inventory_id
    def get_inventory(self, inventory_id):
        for x in self.data:
            if x["id"] == inventory_id:
                return x
        # Return None if inventory_id is not found
        return None

    # Retrieves all inventory records for a specific item_id
    def get_inventories_for_item(self, item_id):
        result = []
        for x in self.data:
            if x["item_id"] == item_id:
                result.append(x)  # Append each inventory that matches the item_id
        return result

    # Aggregates the inventory totals for a specific item_id
    def get_inventory_totals_for_item(self, item_id):
        # Initialize the totals for expected, ordered, allocated, and available
        result = {
            "total_expected": 0,
            "total_ordered": 0,
            "total_allocated": 0,
            "total_available": 0
        }
        # Sum the values across all inventories with the matching item_id
        for x in self.data:
            if x["item_id"] == item_id:
                result["total_expected"] += x["total_expected"]
                result["total_ordered"] += x["total_ordered"]
                result["total_allocated"] += x["total_allocated"]
                result["total_available"] += x["total_available"]
        return result

    # Adds a new inventory entry to the dataset, setting timestamps for creation and update
    def add_inventory(self, inventory):
        inventory["created_at"] = self.get_timestamp()  # Assuming get_timestamp() is implemented in Base class
        inventory["updated_at"] = self.get_timestamp()
        self.data.append(inventory)  # Add the new inventory to the list

    # Updates an existing inventory entry by inventory_id
    def update_inventory(self, inventory_id, inventory):
        inventory["updated_at"] = self.get_timestamp()  # Set updated timestamp
        for i in range(len(self.data)):
            if self.data[i]["id"] == inventory_id:
                self.data[i] = inventory  # Replace old data with updated inventory data
                break

    # Removes an inventory entry by inventory_id
    def remove_inventory(self, inventory_id):
        for x in self.data:
            if x["id"] == inventory_id:
                self.data.remove(x)  # Remove the matching inventory

    # Loads inventory data from JSON file or uses in-memory list if in debug mode
    def load(self, is_debug):
        if is_debug:
            self.data = INVENTORIES  # Use the in-memory list in debug mode
        else:
            f = open(self.data_path, "r")  # Open the inventories.json file in read mode
            self.data = json.load(f)  # Load the JSON data into self.data
            f.close()  # Close the file

    # Saves the inventory data to the inventories.json file
    def save(self):
        f = open(self.data_path, "w")  # Open the inventories.json file in write mode
        json.dump(self.data, f)  # Save the current data as JSON to the file
        f.close()  # Close the file

# import json

# from models.base import Base

# INVENTORIES = []


# class Inventories(Base):
#     def __init__(self, root_path, is_debug=False):
#         self.data_path = root_path + "inventories.json"
#         self.load(is_debug)

#     def get_inventories(self):
#         return self.data

#     def get_inventory(self, inventory_id):
#         for x in self.data:
#             if x["id"] == inventory_id:
#                 return x
#         return None

#     def get_inventories_for_item(self, item_id):
#         result = []
#         for x in self.data:
#             if x["item_id"] == item_id:
#                 result.append(x)
#         return result

#     def get_inventory_totals_for_item(self, item_id):
#         result = {
#             "total_expected": 0,
#             "total_ordered": 0,
#             "total_allocated": 0,
#             "total_available": 0
#         }
#         for x in self.data:
#             if x["item_id"] == item_id:
#                 result["total_expected"] += x["total_expected"]
#                 result["total_ordered"] += x["total_ordered"]
#                 result["total_allocated"] += x["total_allocated"]
#                 result["total_available"] += x["total_available"]
#         return result

#     def add_inventory(self, inventory):
#         inventory["created_at"] = self.get_timestamp()
#         inventory["updated_at"] = self.get_timestamp()
#         self.data.append(inventory)

#     def update_inventory(self, inventory_id, inventory):
#         inventory["updated_at"] = self.get_timestamp()
#         for i in range(len(self.data)):
#             if self.data[i]["id"] == inventory_id:
#                 self.data[i] = inventory
#                 break

#     def remove_inventory(self, inventory_id):
#         for x in self.data:
#             if x["id"] == inventory_id:
#                 self.data.remove(x)

#     def load(self, is_debug):
#         if is_debug:
#             self.data = INVENTORIES
#         else:
#             f = open(self.data_path, "r")
#             self.data = json.load(f)
#             f.close()

#     def save(self):
#         f = open(self.data_path, "w")
#         json.dump(self.data, f)
#         f.close()