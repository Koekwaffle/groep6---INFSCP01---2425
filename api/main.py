import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import socketserver
import http.server
import json
from api.models.warehouses import Warehouses
from api.models.locations import Locations
from api.models.transfers import Transfers
from api.models.items import Items
from api.models.inventories import Inventories
from api.models.suppliers import Suppliers
from api.models.orders import Orders
from api.models.clients import Clients
from api.models.shipments import Shipments

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):
    def send_json_response(self, data, status=200):
        """Send a JSON response."""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def handle_get_version_1(self, path):
        try:
            if path[0] == "warehouses":
                self.handle_warehouses(path[1:])
            elif path[0] == "locations":
                self.handle_locations(path[1:])
            elif path[0] == "transfers":
                self.handle_transfers(path[1:])
            elif path[0] == "items":
                self.handle_items(path[1:])
            elif path[0] == "inventories":
                self.handle_inventories(path[1:])
            elif path[0] == "suppliers":
                self.handle_suppliers(path[1:])
            elif path[0] == "orders":
                self.handle_orders(path[1:])
            elif path[0] == "clients":
                self.handle_clients(path[1:])
            elif path[0] == "shipments":
                self.handle_shipments(path[1:])
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            print(f"Error handling GET request: {e}")
            self.send_response(500)
            self.end_headers()

    def handle_warehouses(self, path):
        model = Warehouses()
        if not path:
            warehouses = model.get_warehouses()
            self.send_json_response(warehouses)
        elif len(path) == 1:
            warehouse_id = int(path[0])
            warehouse = model.get_warehouse(warehouse_id)
            if warehouse:
                self.send_json_response(warehouse)
            else:
                self.send_response(404)
                self.end_headers()
        elif len(path) == 2 and path[1] == "locations":
            location_model = Locations()
            warehouse_id = int(path[0])
            locations = location_model.get_locations_in_warehouse(warehouse_id)
            self.send_json_response(locations)
        else:
            self.send_response(404)
            self.end_headers()

    def handle_locations(self, path):
        model = Locations()
        if not path:
            locations = model.get_locations()
            self.send_json_response(locations)
        elif len(path) == 1:
            location_id = int(path[0])
            location = model.get_location(location_id)
            if location:
                self.send_json_response(location)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_transfers(self, path):
        model = Transfers()
        if not path:
            transfers = model.get_transfers()
            self.send_json_response(transfers)
        elif len(path) == 1:
            transfer_id = int(path[0])
            transfer = model.get_transfer(transfer_id)
            if transfer:
                self.send_json_response(transfer)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_items(self, path):
        model = Items()
        if not path:
            items = model.get_items()
            self.send_json_response(items)
        elif len(path) == 1:
            item_id = int(path[0])
            item = model.get_item(item_id)
            if item:
                self.send_json_response(item)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_inventories(self, path):
        model = Inventories()
        if not path:
            inventories = model.get_inventories()
            self.send_json_response(inventories)
        elif len(path) == 1:
            inventory_id = int(path[0])
            inventory = model.get_inventory(inventory_id)
            if inventory:
                self.send_json_response(inventory)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_suppliers(self, path):
        model = Suppliers()
        if not path:
            suppliers = model.get_suppliers()
            self.send_json_response(suppliers)
        elif len(path) == 1:
            supplier_id = int(path[0])
            supplier = model.get_supplier(supplier_id)
            if supplier:
                self.send_json_response(supplier)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_clients(self, path):
        model = Clients()
        if not path:
            clients = model.get_clients()
            self.send_json_response(clients)
        elif len(path) == 1:
            client_id = int(path[0])
            client = model.get_client(client_id)
            if client:
                self.send_json_response(client)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_shipments(self, path):
        model = Shipments()
        if not path:
            shipments = model.get_shipments()
            self.send_json_response(shipments)
        elif len(path) == 1:
            shipment_id = int(path[0])
            shipment = model.get_shipment(shipment_id)
            if shipment:
                self.send_json_response(shipment)
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_orders(self, path):
        model = Orders()
        try:
            if not path:
                # Handle "Get all orders"
                orders = model.get_orders()
                self.send_json_response(orders)
            elif len(path) == 1:
                # Handle "Get a specific order"
                order_id = int(path[0])
                order = model.get_order(order_id)
                if order:
                    self.send_json_response(order)
                else:
                    self.send_response(404)
                    self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            print(f"Error in handle_orders: {e}")
            self.send_response(500)
            self.end_headers()

    def do_GET(self):
        try:
            path = self.path.strip("/").split("/")
            if len(path) > 1 and path[0] == "api" and path[1] == "v1":
                self.handle_get_version_1(path[2:])
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            print(f"Error processing GET request: {e}")
            self.send_response(500)
            self.end_headers()

if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
