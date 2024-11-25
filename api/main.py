import socketserver
import http.server
import json
from models.warehouses import Warehouses
from models.locations import Locations
from models.transfers import Transfers
from models.items import Items
from models.inventories import Inventories
from models.suppliers import Suppliers
from models.orders import Orders
from models.clients import Clients
from models.shipments import Shipments

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

    # Similar handlers for locations, transfers, items, inventories, suppliers, orders, clients, shipments.

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
