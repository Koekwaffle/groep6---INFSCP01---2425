import sys
import os
import http.server
import json

from api.providers import auth_provider

# Add the parent directory to the system path to access models and processors
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import models
from api.models.clients import Clients
from api.models.contacts import Contacts
from api.models.inventories import Inventories
from api.models.inventory_locations import InventoryLocations
from api.models.item_groups import ItemGroups
from api.models.item_lines import ItemLines
from api.models.item_types import ItemTypes
from api.models.items import Items
from api.models.locations import Locations
from api.models.orders import Orders
from api.models.order_items import OrderItems
from api.models.shipments import Shipments
from api.models.shipment_items import ShipmentItems
from api.models.suppliers import Suppliers
from api.models.transfers import Transfers
from api.models.transfer_items import TransferItems
from api.models.warehouses import Warehouses

# Import retained processors
from api.processors.generic_functions import GenericFunctionsSQLite
from api.processors.inventories_processor import Inventories_processor
from api.processors.items_processor import Items_processor
from api.processors.locations_processor import Locations_processor
from api.processors.orders_processor import Orders_processor
from api.processors.shipments_processor import Shipments_processor
from api.processors.transfers_processor import Transfers_processor
from api.processors.notification_processor import push, start

import logging
logging.basicConfig(level=logging.DEBUG)

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):
    def send_json_response(self, data, status=200):
        """Send a JSON response."""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def parse_path(self):
        """Parse the request path into components."""
        parsed_path = self.path.strip("/").split("/")
        logging.debug(f"Parsed path: {parsed_path}")
        return parsed_path

    def get_user(self):
        """Retrieve the user based on the Authorization header."""
        authorization_header = self.headers.get("Authorization")
        if authorization_header:
            api_key = authorization_header.split(" ")[1]
            return auth_provider.get_user(api_key)
        return None

    def do_GET(self):
        user = self.get_user()
        if user is None:
            self.send_json_response({"error": "Invalid API Key"}, status=403)
            return

        path = self.parse_path()
        if len(path) < 1:
            self.send_json_response({"error": "Invalid path"}, status=400)
            return

        resource = path[0]
        resource_id = path[1] if len(path) > 1 else None

        logging.debug(f"Resource: {resource}, Resource ID: {resource_id}")

        # Map resources to corresponding handlers
        handlers = {
            "clients": Clients,
            "contacts": Contacts,
            "inventories": Inventories_processor,
            "inventory_locations": InventoryLocations,
            "item_groups": ItemGroups,
            "item_lines": ItemLines,
            "item_types": ItemTypes,
            "items": Items_processor,
            "locations": Locations_processor,
            "orders": Orders_processor,
            "order_items": OrderItems,
            "shipments": Shipments_processor,
            "shipment_items": ShipmentItems,
            "suppliers": Suppliers,
            "transfers": Transfers_processor,
            "transfer_items": TransferItems,
            "warehouses": Warehouses,
        }

        if resource in handlers:
            try:
                handler = handlers[resource]()
                if resource_id:
                    response = handler.get(resource_id)
                    logging.debug(f"GET response: {response}")
                    self.send_json_response(response)
                else:
                    response = handler.get_all()
                    logging.debug(f"GET_ALL response: {response}")
                    self.send_json_response(response)
            except Exception as e:
                logging.error(f"Error in GET handler for {resource}: {e}")
                self.send_json_response({"error": str(e)}, status=500)
        else:
            self.send_json_response({"error": "Resource not found"}, status=404)

    def do_POST(self):
        user = self.get_user()
        if user is None:
            self.send_json_response({"error": "Invalid API Key"}, status=403)
            return

        path = self.parse_path()
        if len(path) < 1:
            self.send_json_response({"error": "Invalid path"}, status=400)
            return

        resource = path[0]
        handlers = {
            "clients": Clients,
            "contacts": Contacts,
            "inventories": Inventories_processor,
            "inventory_locations": InventoryLocations,
            "item_groups": ItemGroups,
            "item_lines": ItemLines,
            "item_types": ItemTypes,
            "items": Items_processor,
            "locations": Locations_processor,
            "orders": Orders_processor,
            "order_items": OrderItems,
            "shipments": Shipments_processor,
            "shipment_items": ShipmentItems,
            "suppliers": Suppliers,
            "transfers": Transfers_processor,
            "transfer_items": TransferItems,
            "warehouses": Warehouses,
        }

        if resource in handlers:
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            logging.debug(f"POST data for {resource}: {post_data}")
            try:
                handler = handlers[resource]()
                response = handler.create(post_data)
                logging.debug(f"POST response: {response}")
                self.send_json_response(response, status=201)
            except Exception as e:
                logging.error(f"Error in POST handler for {resource}: {e}")
                self.send_json_response({"error": str(e)}, status=500)
        else:
            self.send_json_response({"error": "Resource not found"}, status=404)

    def do_PUT(self):
        user = self.get_user()
        if user is None:
            self.send_json_response({"error": "Invalid API Key"}, status=403)
            return

        path = self.parse_path()
        if len(path) < 2:
            self.send_json_response({"error": "Invalid path"}, status=400)
            return

        resource = path[0]
        resource_id = path[1]
        handlers = {
            "clients": Clients,
            "contacts": Contacts,
            "inventories": Inventories_processor,
            "inventory_locations": InventoryLocations,
            "item_groups": ItemGroups,
            "item_lines": ItemLines,
            "item_types": ItemTypes,
            "items": Items_processor,
            "locations": Locations_processor,
            "orders": Orders_processor,
            "order_items": OrderItems,
            "shipments": Shipments_processor,
            "shipment_items": ShipmentItems,
            "suppliers": Suppliers,
            "transfers": Transfers_processor,
            "transfer_items": TransferItems,
            "warehouses": Warehouses,
        }

        if resource in handlers:
            content_length = int(self.headers['Content-Length'])
            put_data = json.loads(self.rfile.read(content_length))
            logging.debug(f"PUT data for {resource} with ID {resource_id}: {put_data}")
            try:
                handler = handlers[resource]()
                response = handler.update(resource_id, put_data)
                logging.debug(f"PUT response: {response}")
                self.send_json_response(response)
            except Exception as e:
                logging.error(f"Error in PUT handler for {resource}: {e}")
                self.send_json_response({"error": str(e)}, status=500)
        else:
            self.send_json_response({"error": "Resource not found"}, status=404)

    def do_DELETE(self):
        user = self.get_user()
        if user is None:
            self.send_json_response({"error": "Invalid API Key"}, status=403)
            return

        path = self.parse_path()
        if len(path) < 2:
            self.send_json_response({"error": "Invalid path"}, status=400)
            return

        resource = path[0]
        resource_id = path[1]
        handlers = {
            "clients": Clients,
            "contacts": Contacts,
            "inventories": Inventories_processor,
            "inventory_locations": InventoryLocations,
            "item_groups": ItemGroups,
            "item_lines": ItemLines,
            "item_types": ItemTypes,
            "items": Items_processor,
            "locations": Locations_processor,
            "orders": Orders_processor,
            "order_items": OrderItems,
            "shipments": Shipments_processor,
            "shipment_items": ShipmentItems,
            "suppliers": Suppliers,
            "transfers": Transfers_processor,
            "transfer_items": TransferItems,
            "warehouses": Warehouses,
        }

        if resource in handlers:
            logging.debug(f"DELETE request for {resource} with ID {resource_id}")
            try:
                handler = handlers[resource]()
                response = handler.delete(resource_id)
                logging.debug(f"DELETE response: {response}")
                self.send_json_response(response)
            except Exception as e:
                logging.error(f"Error in DELETE handler for {resource}: {e}")
                self.send_json_response({"error": str(e)}, status=500)
        else:
            self.send_json_response({"error": "Resource not found"}, status=404)

if __name__ == "__main__":
    port = 8080
    server = http.server.HTTPServer(("", port), ApiRequestHandler)
    print(f"Server running on port {port}...")
    start()  # Start the notification processor
    server.serve_forever()
