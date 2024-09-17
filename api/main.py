import socketserver
import http.server
import json

from providers import auth_provider
from providers import data_provider
from processors import notification_processor

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):
    # Handles GET requests for version 1 of the API
    def handle_get_version_1(self, path, user):
        # Check if the user has access to the requested resource
        if not auth_provider.has_access(user, path, "get"):
            self.send_response(403)  # Forbidden
            self.end_headers()
            return

        # Handle different API endpoints based on the path
        if path[0] == "warehouses":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/warehouses
                    # Fetch and return all warehouses
                    warehouses = data_provider.fetch_warehouse_pool().get_warehouses()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouses).encode("utf-8"))
                case 2:  # /api/v1/warehouses/{warehouse_id}
                    # Fetch and return a specific warehouse by ID
                    warehouse_id = int(path[1])
                    warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouse).encode("utf-8"))
                case 3:  # /api/v1/warehouses/{warehouse_id}/locations
                    # Fetch and return locations in a specific warehouse
                    if path[2] == "locations":
                        warehouse_id = int(path[1])
                        locations = data_provider.fetch_location_pool().get_locations_in_warehouse(warehouse_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(locations).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "locations":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/locations
                    # Fetch and return all locations
                    locations = data_provider.fetch_location_pool().get_locations()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(locations).encode("utf-8"))
                case 2:  # /api/v1/locations/{location_id}
                    # Fetch and return a specific location by ID
                    location_id = int(path[1])
                    location = data_provider.fetch_location_pool().get_location(location_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(location).encode("utf-8"))
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "transfers":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/transfers
                    # Fetch and return all transfers
                    transfers = data_provider.fetch_transfer_pool().get_transfers()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfers).encode("utf-8"))
                case 2:  # /api/v1/transfers/{transfer_id}
                    # Fetch and return a specific transfer by ID
                    transfer_id = int(path[1])
                    transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfer).encode("utf-8"))
                case 3:  # /api/v1/transfers/{transfer_id}/items
                    # Fetch and return items in a specific transfer
                    if path[2] == "items":
                        transfer_id = int(path[1])
                        items = data_provider.fetch_transfer_pool().get_items_in_transfer(transfer_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "items":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/items
                    # Fetch and return all items
                    items = data_provider.fetch_item_pool().get_items()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(items).encode("utf-8"))
                case 2:  # /api/v1/items/{item_id}
                    # Fetch and return a specific item by ID
                    item_id = path[1]
                    item = data_provider.fetch_item_pool().get_item(item_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item).encode("utf-8"))
                case 3:  # /api/v1/items/{item_id}/inventory
                    # Fetch and return inventories for a specific item
                    if path[2] == "inventory":
                        item_id = path[1]
                        inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(item_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(inventories).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case 4:  # /api/v1/items/{item_id}/inventory/totals
                    # Fetch and return total inventory for a specific item
                    if path[2] == "inventory" and path[3] == "totals":
                        item_id = path[1]
                        totals = data_provider.fetch_inventory_pool().get_inventory_totals_for_item(item_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(totals).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "item_lines":
            paths = len(path)
            print(paths, path)  # Debug output for path length and content

            match paths:
                case 1:  # /api/v1/item_lines
                    # Fetch and return all item lines
                    item_lines = data_provider.fetch_item_line_pool().get_item_lines()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_lines).encode("utf-8"))
                case 2:  # /api/v1/item_lines/{item_line_id}
                    # Fetch and return a specific item line by ID
                    item_line_id = int(path[1])
                    item_line = data_provider.fetch_item_line_pool().get_item_line(item_line_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_line).encode("utf-8"))
                case 3:  # /api/v1/item_lines/{item_line_id}/items
                    # Fetch and return items for a specific item line
                    if path[2] == "items":
                        item_line_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_line(item_line_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "item_groups":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/item_groups
                    # Fetch and return all item groups
                    item_groups = data_provider.fetch_item_group_pool().get_item_groups()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_groups).encode("utf-8"))
                case 2:  # /api/v1/item_groups/{item_group_id}
                    # Fetch and return a specific item group by ID
                    item_group_id = int(path[1])
                    item_group = data_provider.fetch_item_group_pool().get_item_group(item_group_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_group).encode("utf-8"))
                case 3:  # /api/v1/item_groups/{item_group_id}/items
                    # Fetch and return items for a specific item group
                    if path[2] == "items":
                        item_group_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_group(item_group_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "item_types":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/item_types
                    # Fetch and return all item types
                    item_types = data_provider.fetch_item_type_pool().get_item_types()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_types).encode("utf-8"))
                case 2:  # /api/v1/item_types/{item_type_id}
                    # Fetch and return a specific item type by ID
                    item_type_id = int(path[1])
                    item_type = data_provider.fetch_item_type_pool().get_item_type(item_type_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_type).encode("utf-8"))
                case 3:  # /api/v1/item_types/{item_type_id}/items
                    # Fetch and return items for a specific item type
                    if path[2] == "items":
                        item_type_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_type(item_type_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "inventories":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/inventories
                    # Fetch and return all inventories
                    inventories = data_provider.fetch_inventory_pool().get_inventories()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventories).encode("utf-8"))
                case 2:  # /api/v1/inventories/{inventory_id}
                    # Fetch and return a specific inventory by ID
                    inventory_id = int(path[1])
                    inventory = data_provider.fetch_inventory_pool().get_inventory(inventory_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventory).encode("utf-8"))
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "suppliers":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/suppliers
                    # Fetch and return all suppliers
                    suppliers = data_provider.fetch_supplier_pool().get_suppliers()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(suppliers).encode("utf-8"))
                case 2:  # /api/v1/suppliers/{supplier_id}
                    # Fetch and return a specific supplier by ID
                    supplier_id = int(path[1])
                    supplier = data_provider.fetch_supplier_pool().get_supplier(supplier_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(supplier).encode("utf-8"))
                case 3:  # /api/v1/suppliers/{supplier_id}/items
                    # Fetch and return items for a specific supplier
                    if path[2] == "items":
                        supplier_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_supplier(supplier_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 1:  # /api/v1/orders
                    # Fetch and return all orders
                    orders = data_provider.fetch_order_pool().get_orders()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(orders).encode("utf-8"))
                case 2:  # /api/v1/orders/{order_id}
                    # Fetch and return a specific order by ID
                    order_id = int(path[1])
                    order = data_provider.fetch_order_pool().get_order(order_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(order).encode("utf-8"))
                case 3:  # /api/v1/orders/{order_id}/items
                    # Fetch and return items in a specific order
                    if path[2] == "items":
                        order_id = int(path[1])
                        items = data_provider.fetch_order_pool().get_items_in_order(order_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    self.send_response(404)  # Not Found
                    self.end_headers()

        # Handle GET requests based on the requested path
        elif path[0] == "clients":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return the list of all clients
                    clients = data_provider.fetch_client_pool().get_clients()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(clients).encode("utf-8"))
                case 2:
                    # Fetch and return a specific client by ID
                    client_id = int(path[1])
                    client = data_provider.fetch_client_pool().get_client(client_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(client).encode("utf-8"))
                case 3:
                    if path[2] == "orders":
                        # Fetch and return orders for a specific client
                        client_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_for_client(client_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    else:
                        # Path is not recognized
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    # Path length does not match expected cases
                    self.send_response(404)  # Not Found
                    self.end_headers()

        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 1:
                    # Fetch and return the list of all shipments
                    shipments = data_provider.fetch_shipment_pool().get_shipments()
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipments).encode("utf-8"))
                case 2:
                    # Fetch and return a specific shipment by ID
                    shipment_id = int(path[1])
                    shipment = data_provider.fetch_shipment_pool().get_shipment(shipment_id)
                    self.send_response(200)  # OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipment).encode("utf-8"))
                case 3:
                    if path[2] == "orders":
                        # Fetch and return orders in a specific shipment
                        shipment_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_in_shipment(shipment_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    elif path[2] == "items":
                        # Fetch and return items in a specific shipment
                        shipment_id = int(path[1])
                        items = data_provider.fetch_shipment_pool().get_items_in_shipment(shipment_id)
                        self.send_response(200)  # OK
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        # Path is not recognized
                        self.send_response(404)  # Not Found
                        self.end_headers()
                case _:
                    # Path length does not match expected cases
                    self.send_response(404)  # Not Found
                    self.end_headers()

        else:
            # Path does not match any recognized routes
            self.send_response(404)  # Not Found
            self.end_headers()

        # Handle POST requests based on the requested path
        def handle_post_version_1(self, path, user):
            if not auth_provider.has_access(user, path, "post"):
                self.send_response(403)  # Forbidden
                self.end_headers()
                return

            # Read and decode the POST request data
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_data = json.loads(post_data.decode())

            # Process POST requests based on the path
            if path[0] == "warehouses":
                # Add a new warehouse
                data_provider.fetch_warehouse_pool().add_warehouse(new_data)
                data_provider.fetch_warehouse_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "locations":
                # Add a new location
                data_provider.fetch_location_pool().add_location(new_data)
                data_provider.fetch_location_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "transfers":
                # Add a new transfer and notify
                data_provider.fetch_transfer_pool().add_transfer(new_data)
                data_provider.fetch_transfer_pool().save()
                notification_processor.push(f"Scheduled batch transfer {new_data['id']}")
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "items":
                # Add a new item
                data_provider.fetch_item_pool().add_item(new_data)
                data_provider.fetch_item_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "inventories":
                # Add new inventory
                data_provider.fetch_inventory_pool().add_inventory(new_data)
                data_provider.fetch_inventory_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "suppliers":
                # Add a new supplier
                data_provider.fetch_supplier_pool().add_supplier(new_data)
                data_provider.fetch_supplier_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "orders":
                # Add a new order
                data_provider.fetch_order_pool().add_order(new_data)
                data_provider.fetch_order_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "clients":
                # Add a new client
                data_provider.fetch_client_pool().add_client(new_data)
                data_provider.fetch_client_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            elif path[0] == "shipments":
                # Add a new shipment
                data_provider.fetch_shipment_pool().add_shipment(new_data)
                data_provider.fetch_shipment_pool().save()
                self.send_response(201)  # Created
                self.end_headers()
            else:
                # Path is not recognized
                self.send_response(404)  # Not Found
                self.end_headers()

        # Handle POST requests
        def do_POST(self):
            api_key = self.headers.get("API_KEY")
            user = auth_provider.get_user(api_key)
            if user == None:
                self.send_response(401)  # Unauthorized
                self.end_headers()
            else:
                try:
                    path = self.path.split("/")
                    if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                        self.handle_post_version_1(path[3:], user)
                except Exception:
                    self.send_response(500)  # Internal Server Error
                    self.end_headers()

# Handle PUT requests for version 1 of the API
def handle_put_version_1(self, path, user):
    # Check if the user has permission to perform a PUT operation
    if not auth_provider.has_access(user, path, "put"):
        self.send_response(403)  # Forbidden
        self.end_headers()
        return

    # Handle different types of PUT requests based on the path
    if path[0] == "warehouses":
        # Update a specific warehouse
        warehouse_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_warehouse = json.loads(post_data.decode())
        data_provider.fetch_warehouse_pool().update_warehouse(warehouse_id, updated_warehouse)
        data_provider.fetch_warehouse_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "locations":
        # Update a specific location
        location_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_location = json.loads(post_data.decode())
        data_provider.fetch_location_pool().update_location(location_id, updated_location)
        data_provider.fetch_location_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "transfers":
        # Handle PUT requests for transfers with different path lengths
        paths = len(path)
        match paths:
            case 2:
                # Update a specific transfer
                transfer_id = int(path[1])
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                updated_transfer = json.loads(post_data.decode())
                data_provider.fetch_transfer_pool().update_transfer(transfer_id, updated_transfer)
                data_provider.fetch_transfer_pool().save()
                self.send_response(200)  # OK
                self.end_headers()
            
            case 3:
                if path[2] == "commit":
                    # Commit a transfer and update inventories
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
                    self.send_response(200)  # OK
                    self.end_headers()
                else:
                    # Unrecognized path segment
                    self.send_response(404)  # Not Found
                    self.end_headers()
            
            case _:
                # Path length does not match expected cases
                self.send_response(404)  # Not Found
                self.end_headers()
    
    elif path[0] == "items":
        # Update a specific item
        item_id = path[1]
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_item = json.loads(post_data.decode())
        data_provider.fetch_item_pool().update_item(item_id, updated_item)
        data_provider.fetch_item_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "item_lines":
        # Update a specific item line
        item_line_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_item_line = json.loads(post_data.decode())
        data_provider.fetch_item_line_pool().update_item_line(item_line_id, updated_item_line)
        data_provider.fetch_item_line_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "item_groups":
        # Update a specific item group
        item_group_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_item_group = json.loads(post_data.decode())
        data_provider.fetch_item_group_pool().update_item_group(item_group_id, updated_item_group)
        data_provider.fetch_item_group_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "item_types":
        # Update a specific item type
        item_type_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_item_type = json.loads(post_data.decode())
        data_provider.fetch_item_type_pool().update_item_type(item_type_id, updated_item_type)
        data_provider.fetch_item_type_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "inventories":
        # Update a specific inventory
        inventory_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_inventory = json.loads(post_data.decode())
        data_provider.fetch_inventory_pool().update_inventory(inventory_id, updated_inventory)
        data_provider.fetch_inventory_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "suppliers":
        # Update a specific supplier
        supplier_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_supplier = json.loads(post_data.decode())
        data_provider.fetch_supplier_pool().update_supplier(supplier_id, updated_supplier)
        data_provider.fetch_supplier_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "orders":
        # Handle PUT requests for orders with different path lengths
        paths = len(path)
        match paths:
            case 2:
                # Update a specific order
                order_id = int(path[1])
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                updated_order = json.loads(post_data.decode())
                data_provider.fetch_order_pool().update_order(order_id, updated_order)
                data_provider.fetch_order_pool().save()
                self.send_response(200)  # OK
                self.end_headers()
            
            case 3:
                if path[2] == "items":
                    # Update items in a specific order
                    order_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_items = json.loads(post_data.decode())
                    data_provider.fetch_order_pool().update_items_in_order(order_id, updated_items)
                    data_provider.fetch_order_pool().save()
                    self.send_response(200)  # OK
                    self.end_headers()
                else:
                    # Unrecognized path segment
                    self.send_response(404)  # Not Found
                    self.end_headers()
            
            case _:
                # Path length does not match expected cases
                self.send_response(404)  # Not Found
                self.end_headers()
    
    elif path[0] == "clients":
        # Update a specific client
        client_id = int(path[1])
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        updated_client = json.loads(post_data.decode())
        data_provider.fetch_client_pool().update_client(client_id, updated_client)
        data_provider.fetch_client_pool().save()
        self.send_response(200)  # OK
        self.end_headers()
    
    elif path[0] == "shipments":
        # Handle PUT requests for shipments with different path lengths
        paths = len(path)
        match paths:
            case 2:
                # Update a specific shipment
                shipment_id = int(path[1])
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                updated_shipment = json.loads(post_data.decode())
                data_provider.fetch_shipment_pool().update_shipment(shipment_id, updated_shipment)
                data_provider.fetch_shipment_pool().save()
                self.send_response(200)  # OK
                self.end_headers()
            
            case 3:
                if path[2] == "orders":
                    # Update orders in a specific shipment
                    shipment_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_orders = json.loads(post_data.decode())
                    data_provider.fetch_order_pool().update_orders_in_shipment(shipment_id, updated_orders)
                    data_provider.fetch_order_pool().save()
                    self.send_response(200)  # OK
                    self.end_headers()
                elif path[2] == "items":
                    # Update items in a specific shipment
                    shipment_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_items = json.loads(post_data.decode())
                    data_provider.fetch_shipment_pool().update_items_in_shipment(shipment_id, updated_items)
                    data_provider.fetch_shipment_pool().save()
                    self.send_response(200)  # OK
                    self.end_headers()
                elif path[2] == "commit":
                    # No action defined for "commit" in this context
                    pass
                else:
                    # Unrecognized path segment
                    self.send_response(404)  # Not Found
                    self.end_headers()
            
            case _:
                # Path length does not match expected cases
                self.send_response(404)  # Not Found
                self.end_headers()
    
    else:
        # Unrecognized path
        self.send_response(404)  # Not Found
        self.end_headers()

# Handle DELETE requests
def do_DELETE(self):
    # Get the API key and retrieve the user
    api_key = self.headers.get("API_KEY")
    user = auth_provider.get_user(api_key)
    if user is None:
        self.send_response(401)  # Unauthorized
        self.end_headers()
    else:
        try:
            # Split the path and check if it matches the expected format
            path = self.path.split("/")
            if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                self.handle_delete_version_1(path[3:], user)
        except Exception:
            # Handle unexpected errors
            self.send_response(500)  # Internal Server Error
            self.end_headers()

# Handle PUT requests
def do_PUT(self):
    # Get the API key and retrieve the user
    api_key = self.headers.get("API_KEY")
    user = auth_provider.get_user(api_key)
    if user is None:
        self.send_response(401)  # Unauthorized
        self.end_headers()
    else:
        try:
            # Split the path and check if it matches the expected format
            path = self.path.split("/")
            if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                self.handle_put_version_1(path[3:], user)
        except Exception:
            # Handle unexpected errors
            self.send_response(500)  # Internal Server Error
            self.end_headers()

# Main function to start the server
if __name__ == "__main__":
    PORT = 3000
    # Create and start the server
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        auth_provider.init()  # Initialize the authentication provider
        data_provider.init()  # Initialize the data provider
        notification_processor.start()  # Start the notification processor
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()  # Run the server
