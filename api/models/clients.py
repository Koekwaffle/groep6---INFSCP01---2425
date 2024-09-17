import json

from models.base import Base

# List that stores clients if the 'is_debug' flag is set to True
CLIENTS = []


class Clients(Base):
    def __init__(self, root_path, is_debug=False):
        # Set the path to the clients.json file based on the provided root_path
        self.data_path = root_path + "clients.json"
        # Load the data from file or debug clients list
        self.load(is_debug)

    # Returns all client data
    def get_clients(self):
        return self.data

    # Retrieve a single client by client_id
    def get_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                return x
        # Return None if the client ID does not exist
        return None

    # Adds a new client to the data, setting creation and update timestamps
    def add_client(self, client):
        client["created_at"] = self.get_timestamp()  # Assuming get_timestamp() is implemented in Base class
        client["updated_at"] = self.get_timestamp()
        self.data.append(client)  # Append the new client to the data list

    # Update an existing client by client_id
    def update_client(self, client_id, client):
        client["updated_at"] = self.get_timestamp()  # Update the timestamp for modification
        for i in range(len(self.data)):
            if self.data[i]["id"] == client_id:
                self.data[i] = client  # Replace the old client data with the updated data
                break

    # Remove a client by client_id
    def remove_client(self, client_id):
        for x in self.data:
            if x["id"] == client_id:
                self.data.remove(x)  # Remove the client from the data list

    # Load client data from JSON file or use in-memory clients list if debug mode is enabled
    def load(self, is_debug):
        if is_debug:
            self.data = CLIENTS  # Use global CLIENTS if in debug mode
        else:
            f = open(self.data_path, "r")  # Open the clients.json file in read mode
            self.data = json.load(f)  # Load the JSON data from file into self.data
            f.close()  # Close the file

    # Save the client data to the clients.json file
    def save(self):
        f = open(self.data_path, "w")  # Open the clients.json file in write mode
        json.dump(self.data, f)  # Dump the current client data to file as JSON
        f.close()  # Close the file

# import json

# from models.base import Base

# CLIENTS = []


# class Clients(Base):
#     def __init__(self, root_path, is_debug=False):
#         self.data_path = root_path + "clients.json"
#         self.load(is_debug)

#     def get_clients(self):
#         return self.data

#     def get_client(self, client_id):
#         for x in self.data:
#             if x["id"] == client_id:
#                 return x
#         return None

#     def add_client(self, client):
#         client["created_at"] = self.get_timestamp()
#         client["updated_at"] = self.get_timestamp()
#         self.data.append(client)

#     def update_client(self, client_id, client):
#         client["updated_at"] = self.get_timestamp()
#         for i in range(len(self.data)):
#             if self.data[i]["id"] == client_id:
#                 self.data[i] = client
#                 break

#     def remove_client(self, client_id):
#         for x in self.data:
#             if x["id"] == client_id:
#                 self.data.remove(x)

#     def load(self, is_debug):
#         if is_debug:
#             self.data = CLIENTS
#         else:
#             f = open(self.data_path, "r")
#             self.data = json.load(f)
#             f.close()

#     def save(self):
#         f = open(self.data_path, "w")
#         json.dump(self.data, f)
#         f.close()
