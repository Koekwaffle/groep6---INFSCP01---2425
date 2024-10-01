import sys
sys.path.append('/path/to/project_folder')

from processors.warehouses_processor import Warehouses_processor
from processors.locations_processor import Locations_processor
from processors.transfers_processor import Transfers_processor
from processors.items_processor import Items_processor
from processors.item_lines_processor import ItemLines_processor
from processors.item_groups_processor import ItemGroups_processor
from processors.item_types_processor import ItemTypes_processor
from processors.inventories_processor import Inventories_processor
from processors.suppliers_processor import Suppliers_processor
from processors.orders_processor import Orders_processor
from processors.clients_processor import Clients_processor
from processors.shipments_processor import Shipments_processor


DEBUG = False

ROOT_PATH = "./data/"

_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None


def init():
    global _warehouses
    _warehouses = Warehouses_processor(ROOT_PATH, DEBUG)
    global _locations
    _locations = Locations_processor(ROOT_PATH, DEBUG)
    global _transfers
    _transfers = Transfers_processor(ROOT_PATH, DEBUG)
    global _items
    _items = Items_processor(ROOT_PATH, DEBUG)
    global _item_lines
    _item_lines = ItemLines_processor(ROOT_PATH, DEBUG)
    global _item_groups
    _item_groups = ItemGroups_processor(ROOT_PATH, DEBUG)
    global _item_types
    _item_types = ItemTypes_processor(ROOT_PATH, DEBUG)
    global _inventories
    _inventories = Inventories_processor(ROOT_PATH, DEBUG)
    global _suppliers
    _suppliers = Suppliers_processor(ROOT_PATH, DEBUG)
    global _orders
    _orders = Orders_processor(ROOT_PATH, DEBUG)
    global _clients
    _clients = Clients_processor(ROOT_PATH, DEBUG)
    global _shipments
    _shipments = Shipments_processor(ROOT_PATH, DEBUG)


def fetch_warehouse_pool():
    return _warehouses


def fetch_location_pool():
    return _locations


def fetch_transfer_pool():
    return _transfers


def fetch_item_pool():
    return _items


def fetch_item_line_pool():
    return _item_lines


def fetch_item_group_pool():
    return _item_groups


def fetch_item_type_pool():
    return _item_types


def fetch_inventory_pool():
    return _inventories


def fetch_supplier_pool():
    return _suppliers


def fetch_order_pool():
    return _orders


def fetch_client_pool():
    return _clients


def fetch_shipment_pool():
    return _shipments
