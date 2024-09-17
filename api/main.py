import socketserver  # Provides classes for creating socket-based servers
import http.server  # Provides classes for creating HTTP servers
import json  # Provides functionality for working with JSON data

# Import custom modules for handling authentication, data fetching, and processing notifications
from providers import auth_provider
from providers import data_provider
from processors import notification_processor


# Custom handler class that extends BaseHTTPRequestHandler to process API requests
class ApiRequestHandler(http.server.BaseHTTPRequestHandler):

    # Function to handle GET requests for version 1 of the API
    def handle_get_version_1(self, path, user):
        # Check if the user has access to the requested path with "GET" method
        if not auth_provider.has_access(user, path, "get"):  # checks if user has access
            self.send_response(403)  # Respond with a 403 Forbidden if no access
            self.end_headers()
            return
        
        # Handling paths related to "warehouses"
        if path[0] == "warehouses":
            paths = len(path)  # Get the number of parts in the path
            match paths:
                # If path is '/warehouses', return all warehouses
                case 1:
                    warehouses = data_provider.fetch_warehouse_pool().get_warehouses()  # Fetch all warehouses
                    self.send_response(200)  # Respond with 200 OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouses).encode("utf-8"))  # Send the warehouse data as JSON
                # If path is '/warehouses/{warehouse_id}', return specific warehouse
                case 2:
                    warehouse_id = int(path[1])  # Get the warehouse ID from the path
                    warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)  # Fetch warehouse data
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouse).encode("utf-8"))
                # If path is '/warehouses/{warehouse_id}/locations', return locations for a warehouse
                case 3:
                    if path[2] == "locations":
                        warehouse_id = int(path[1])
                        locations = data_provider.fetch_location_pool().get_locations_in_warehouse(warehouse_id)  # Fetch locations in the warehouse
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(locations).encode("utf-8"))
                    else:
                        self.send_response(404)  # Respond with 404 Not Found if path is invalid
                        self.end_headers()
                # If none of the above cases match, respond with 404
                case _:
                    self.send_response(404)
                    self.end_headers()

        # Handling paths related to "locations"
        elif path[0] == "locations":
            paths = len(path)
            match paths:
                # If path is '/locations', return all locations
                case 1:
                    locations = data_provider.fetch_location_pool().get_locations()  # Fetch all locations
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(locations).encode("utf-8"))
                # If path is '/locations/{location_id}', return specific location
                case 2:
                    location_id = int(path[1])
                    location = data_provider.fetch_location_pool().get_location(location_id)  # Fetch location data
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(location).encode("utf-8"))
                # If none of the above cases match, respond with 404
                case _:
                    self.send_response(404)
                    self.end_headers()

        # Handling paths related to "transfers"
        elif path[0] == "transfers":
            paths = len(path)
            match paths:
                # If path is '/transfers', return all transfers
                case 1:
                    transfers = data_provider.fetch_transfer_pool().get_transfers()  # Fetch all transfers
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfers).encode("utf-8"))
                # If path is '/transfers/{transfer_id}', return specific transfer
                case 2:
                    transfer_id = int(path[1])
                    transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)  # Fetch transfer data
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfer).encode("utf-8"))
                # If path is '/transfers/{transfer_id}/items', return items in a specific transfer
                case 3:
                    if path[2] == "items":
                        transfer_id = int(path[1])
                        items = data_provider.fetch_transfer_pool().get_items_in_transfer(transfer_id)  # Fetch items in the transfer
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Respond with 404 if the path is invalid
                        self.end_headers()
                # If none of the above cases match, respond with 404
                case _:
                    self.send_response(404)
                    self.end_headers()

        # Handling paths related to "items"
        elif path[0] == "items":
            paths = len(path)
            match paths:
                # If path is '/items', return all items
                case 1:
                    items = data_provider.fetch_item_pool().get_items()  # Fetch all items
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(items).encode("utf-8"))
                # If path is '/items/{item_id}', return specific item
                case 2:
                    item_id = path[1]
                    item = data_provider.fetch_item_pool().get_item(item_id)  # Fetch item data
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item).encode("utf-8"))
                # If path is '/items/{item_id}/inventory', return inventory for a specific item
                case 3:
                    if path[2] == "inventory":
                        item_id = path[1]
                        inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(item_id)  # Fetch inventories for the item
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(inventories).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                # If path is '/items/{item_id}/inventory/totals', return inventory totals for a specific item
                case 4:
                    if path[2] == "inventory" and path[3] == "totals":
                        item_id = path[1]
                        totals = data_provider.fetch_inventory_pool().get_inventory_totals_for_item(item_id)  # Fetch inventory totals
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(totals).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                # If none of the above cases match, respond with 404
                case _:
                    self.send_response(404)
                    self.end_headers()

        # Handling paths related to "item_lines"
        elif path[0] == "item_lines":
            paths = len(path)
            print(paths, path)  # Debugging: print the path to the console

# Check if the first part of the path is "item_lines"
if path[0] == "item_lines":
    paths = len(path)  # Get the length of the path
    match paths:  # Match the length of the path
        case 1:
            # If the path has only "item_lines", fetch and return all item lines
            item_lines = data_provider.fetch_item_line_pool().get_item_lines()
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_lines).encode("utf-8"))  # Send the item lines as a JSON response
        case 2:
            # If the path has "item_lines/{item_line_id}", fetch and return details of a specific item line
            item_line_id = int(path[1])
            item_line = data_provider.fetch_item_line_pool().get_item_line(item_line_id)
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_line).encode("utf-8"))  # Send the specific item line details
        case 3:
            # If the path is "item_lines/{item_line_id}/items", fetch and return the items for the specific item line
            if path[2] == "items":
                item_line_id = int(path[1])
                items = data_provider.fetch_item_pool().get_items_for_item_line(item_line_id)
                self.send_response(200)  # Send a 200 OK response
                self.send_header("Content-type", "application/json")  # Set response content-type as JSON
                self.end_headers()  # End headers
                self.wfile.write(json.dumps(items).encode("utf-8"))  # Send the items as a JSON response
            else:
                # If the third part of the path is invalid, return a 404 Not Found
                self.send_response(404)
                self.end_headers()
        case _:
            # If the path length doesn't match any valid case, return a 404 Not Found
            self.send_response(404)
            self.end_headers()

# Handling the "item_groups" endpoint
elif path[0] == "item_groups":
    paths = len(path)  # Get the length of the path
    match paths:
        case 1:
            # If the path has only "item_groups", fetch and return all item groups
            item_groups = data_provider.fetch_item_group_pool().get_item_groups()
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_groups).encode("utf-8"))  # Send item groups as JSON response
        case 2:
            # If the path has "item_groups/{item_group_id}", fetch and return details of a specific item group
            item_group_id = int(path[1])
            item_group = data_provider.fetch_item_group_pool().get_item_group(item_group_id)
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_group).encode("utf-8"))  # Send the specific item group details
        case 3:
            # If the path is "item_groups/{item_group_id}/items", fetch and return the items for the specific item group
            if path[2] == "items":
                item_group_id = int(path[1])
                items = data_provider.fetch_item_pool().get_items_for_item_group(item_group_id)
                self.send_response(200)  # Send a 200 OK response
                self.send_header("Content-type", "application/json")  # Set response content-type as JSON
                self.end_headers()  # End headers
                self.wfile.write(json.dumps(items).encode("utf-8"))  # Send the items as JSON response
            else:
                # If the third part of the path is invalid, return a 404 Not Found
                self.send_response(404)
                self.end_headers()
        case _:
            # If the path length doesn't match any valid case, return a 404 Not Found
            self.send_response(404)
            self.end_headers()

# Handling the "item_types" endpoint
elif path[0] == "item_types":
    paths = len(path)  # Get the length of the path
    match paths:
        case 1:
            # If the path has only "item_types", fetch and return all item types
            item_types = data_provider.fetch_item_type_pool().get_item_types()
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_types).encode("utf-8"))  # Send item types as JSON response
        case 2:
            # If the path has "item_types/{item_type_id}", fetch and return details of a specific item type
            item_type_id = int(path[1])
            item_type = data_provider.fetch_item_type_pool().get_item_type(item_type_id)
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(item_type).encode("utf-8"))  # Send the specific item type details
        case 3:
            # If the path is "item_types/{item_type_id}/items", fetch and return the items for the specific item type
            if path[2] == "items":
                item_type_id = int(path[1])
                items = data_provider.fetch_item_pool().get_items_for_item_type(item_type_id)
                self.send_response(200)  # Send a 200 OK response
                self.send_header("Content-type", "application/json")  # Set response content-type as JSON
                self.end_headers()  # End headers
                self.wfile.write(json.dumps(items).encode("utf-8"))  # Send the items as JSON response
            else:
                # If the third part of the path is invalid, return a 404 Not Found
                self.send_response(404)
                self.end_headers()
        case _:
            # If the path length doesn't match any valid case, return a 404 Not Found
            self.send_response(404)
            self.end_headers()

# Handling the "inventories" endpoint
elif path[0] == "inventories":
    paths = len(path)  # Get the length of the path
    match paths:
        case 1:
            # If the path has only "inventories", fetch and return all inventories
            inventories = data_provider.fetch_inventory_pool().get_inventories()
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(inventories).encode("utf-8"))  # Send inventories as JSON response
        case 2:
            # If the path has "inventories/{inventory_id}", fetch and return details of a specific inventory
            inventory_id = int(path[1])
            inventory = data_provider.fetch_inventory_pool().get_inventory(inventory_id)
            self.send_response(200)  # Send a 200 OK response
            self.send_header("Content-type", "application/json")  # Set response content-type as JSON
            self.end_headers()  # End headers
            self.wfile.write(json.dumps(inventory).encode("utf-8"))  # Send the specific inventory details
        case _:
            # If the path length doesn't match any valid case, return a 404 Not Found
            self.send_response(404)
            self.end_headers()

# The rest of the blocks handle "suppliers", "orders", "clients", and "shipments" similarly.
# They match the path and respond with the appropriate data in JSON format, or a 404 error if the path is invalid.


    def do_GET(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_get_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_post_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "post"):
            self.send_response(403)
            self.end_headers()
            return
        if path[0] == "warehouses":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_warehouse = json.loads(post_data.decode())
            data_provider.fetch_warehouse_pool().add_warehouse(new_warehouse)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "locations":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_location = json.loads(post_data.decode())
            data_provider.fetch_location_pool().add_location(new_location)
            data_provider.fetch_location_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "transfers":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_transfer = json.loads(post_data.decode())
            data_provider.fetch_transfer_pool().add_transfer(new_transfer)
            data_provider.fetch_transfer_pool().save()
            notification_processor.push(f"Scheduled batch transfer {new_transfer['id']}")
            self.send_response(201)
            self.end_headers()
        elif path[0] == "items":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_item = json.loads(post_data.decode())
            data_provider.fetch_item_pool().add_item(new_item)
            data_provider.fetch_item_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "inventories":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_inventory = json.loads(post_data.decode())
            data_provider.fetch_inventory_pool().add_inventory(new_inventory)
            data_provider.fetch_inventory_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "suppliers":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_supplier = json.loads(post_data.decode())
            data_provider.fetch_supplier_pool().add_supplier(new_supplier)
            data_provider.fetch_supplier_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "orders":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_order = json.loads(post_data.decode())
            data_provider.fetch_order_pool().add_order(new_order)
            data_provider.fetch_order_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "clients":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_client = json.loads(post_data.decode())
            data_provider.fetch_client_pool().add_client(new_client)
            data_provider.fetch_client_pool().save()
            self.send_response(201)
            self.end_headers()
        elif path[0] == "shipments":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_shipment = json.loads(post_data.decode())
            data_provider.fetch_shipment_pool().add_shipment(new_shipment)
            data_provider.fetch_shipment_pool().save()
            self.send_response(201)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_post_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_put_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "put"):
            self.send_response(403)
            self.end_headers()
            return
        if path[0] == "warehouses":
            warehouse_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_warehouse = json.loads(post_data.decode())
            data_provider.fetch_warehouse_pool().update_warehouse(warehouse_id, updated_warehouse)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "locations":
            location_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_location = json.loads(post_data.decode())
            data_provider.fetch_location_pool().update_location(location_id, updated_location)
            data_provider.fetch_location_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "transfers":
            paths = len(path)
            match paths:
                case 2:
                    transfer_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_transfer = json.loads(post_data.decode())
                    data_provider.fetch_transfer_pool().update_transfer(transfer_id, updated_transfer)
                    data_provider.fetch_transfer_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "commit":
                        transfer_id = int(path[1])
                        transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
                        for x in transfer["items"]:
                            inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(x["item_id"])
                            for y in inventories:
                                if y["location_id"] == transfer["transfer_from"]:
                                    y["total_on_hand"] -= x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_inventory_pool().update_inventory(y["id"], y)
                                elif y["location_id"] == transfer["transfer_to"]:
                                    y["total_on_hand"] += x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_inventory_pool().update_inventory(y["id"], y)
                        transfer["transfer_status"] = "Processed"
                        data_provider.fetch_transfer_pool().update_transfer(transfer_id, transfer)
                        notification_processor.push(f"Processed batch transfer with id:{transfer['id']}")
                        data_provider.fetch_transfer_pool().save()
                        data_provider.fetch_inventory_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "items":
            item_id = path[1]
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item = json.loads(post_data.decode())
            data_provider.fetch_item_pool().update_item(item_id, updated_item)
            data_provider.fetch_item_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_lines":
            item_line_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_line = json.loads(post_data.decode())
            data_provider.fetch_item_line_pool().update_item_line(item_line_id, updated_item_line)
            data_provider.fetch_item_line_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_groups":
            item_group_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_group = json.loads(post_data.decode())
            data_provider.fetch_item_group_pool().update_item_group(item_group_id, updated_item_group)
            data_provider.fetch_item_group_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_types":
            item_type_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_item_type = json.loads(post_data.decode())
            data_provider.fetch_item_type_pool().update_item_type(item_type_id, updated_item_type)
            data_provider.fetch_item_type_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "inventories":
            inventory_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_inventory = json.loads(post_data.decode())
            data_provider.fetch_inventory_pool().update_inventory(inventory_id, updated_inventory)
            data_provider.fetch_inventory_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "suppliers":
            supplier_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_supplier = json.loads(post_data.decode())
            data_provider.fetch_supplier_pool().update_supplier(supplier_id, updated_supplier)
            data_provider.fetch_supplier_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 2:
                    order_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_order = json.loads(post_data.decode())
                    data_provider.fetch_order_pool().update_order(order_id, updated_order)
                    data_provider.fetch_order_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "items":
                        order_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_order_pool().update_items_in_order(order_id, updated_items)
                        data_provider.fetch_order_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "clients":
            client_id = int(path[1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            updated_client = json.loads(post_data.decode())
            data_provider.fetch_client_pool().update_client(client_id, updated_client)
            data_provider.fetch_client_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 2:
                    shipment_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_shipment = json.loads(post_data.decode())
                    data_provider.fetch_shipment_pool().update_shipment(shipment_id, updated_shipment)
                    data_provider.fetch_shipment_pool().save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "orders":
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_orders = json.loads(post_data.decode())
                        data_provider.fetch_order_pool().update_orders_in_shipment(shipment_id, updated_orders)
                        data_provider.fetch_order_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "items":
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_shipment_pool().update_items_in_shipment(shipment_id, updated_items)
                        data_provider.fetch_shipment_pool().save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "commit":
                        pass
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_put_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_delete_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "delete"):
            self.send_response(403)
            self.end_headers()
            return
        if path[0] == "warehouses":
            warehouse_id = int(path[1])
            data_provider.fetch_warehouse_pool().remove_warehouse(warehouse_id)
            data_provider.fetch_warehouse_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "locations":
            location_id = int(path[1])
            data_provider.fetch_location_pool().remove_location(location_id)
            data_provider.fetch_location_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "transfers":
            transfer_id = int(path[1])
            data_provider.fetch_transfer_pool().remove_transfer(transfer_id)
            data_provider.fetch_transfer_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "items":
            item_id = path[1]
            data_provider.fetch_item_pool().remove_item(item_id)
            data_provider.fetch_item_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_lines":
            item_line_id = int(path[1])
            data_provider.fetch_item_line_pool().remove_item_line(item_line_id)
            data_provider.fetch_item_line_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_groups":
            item_group_id = int(path[1])
            data_provider.fetch_item_group_pool().remove_item_group(item_group_id)
            data_provider.fetch_item_group_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "item_types":
            item_type_id = int(path[1])
            data_provider.fetch_item_type_pool().remove_item_type(item_type_id)
            data_provider.fetch_item_type_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "inventories":
            inventory_id = int(path[1])
            data_provider.fetch_inventory_pool().remove_inventory(inventory_id)
            data_provider.fetch_inventory_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "suppliers":
            supplier_id = int(path[1])
            data_provider.fetch_supplier_pool().remove_supplier(supplier_id)
            data_provider.fetch_supplier_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "orders":
            order_id = int(path[1])
            data_provider.fetch_order_pool().remove_order(order_id)
            data_provider.fetch_order_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "clients":
            client_id = int(path[1])
            data_provider.fetch_client_pool().remove_client(client_id)
            data_provider.fetch_client_pool().save()
            self.send_response(200)
            self.end_headers()
        elif path[0] == "shipments":
            shipment_id = int(path[1])
            data_provider.fetch_shipment_pool().remove_shipment(shipment_id)
            data_provider.fetch_shipment_pool().save()
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_delete_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()


if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        auth_provider.init()
        data_provider.init()
        notification_processor.start()
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
