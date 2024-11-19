CREATE TABLE clients (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  city TEXT,
  zip_code TEXT,
  province TEXT,
  country TEXT,
  contact_name TEXT,
  contact_phone TEXT,
  contact_email TEXT,
  updated_at TEXT,
  created_at TEXT
);

CREATE TABLE contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  warehouse_id INTEGER NOT NULL,
  name TEXT,
  phone TEXT,
  email TEXT,
  FOREIGN KEY (warehouse_id) REFERENCES warehouses (id)
);

CREATE TABLE inventories (
  id INTEGER PRIMARY KEY,
  item_id TEXT,
  description TEXT,
  item_reference TEXT,
  location_id INTEGER,
  total_on_hand INTEGER,
  total_expected INTEGER,
  total_ordered INTEGER,
  total_allocated INTEGER,
  total_available INTEGER,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (location_id) REFERENCES locations (id)
);

CREATE TABLE inventory_locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  inventory_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  FOREIGN KEY (inventory_id) REFERENCES inventories (id),
  FOREIGN KEY (location_id) REFERENCES locations (id)
);

CREATE TABLE item_groups (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE item_line (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE item_types (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE items (
  uid TEXT PRIMARY KEY,
  code TEXT,
  description TEXT,
  short_description TEXT,
  upc_code TEXT,
  model_number TEXT,
  commodity_code TEXT,
  item_line INTEGER,
  item_group INTEGER,
  item_type INTEGER,
  unit_purchase_quantity INTEGER,
  unit_order_quantity INTEGER,
  pack_order_quantity INTEGER,
  supplier_id INTEGER,
  supplier_code TEXT,
  supplier_part_number TEXT,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (item_line) REFERENCES item_line (id),
  FOREIGN KEY (item_group) REFERENCES item_groups (id),
  FOREIGN KEY (item_type) REFERENCES item_types (id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
);

CREATE TABLE locations (
  id INTEGER PRIMARY KEY,
  warehouse_id INTEGER,
  code TEXT,
  name TEXT,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (warehouse_id) REFERENCES warehouses (id)
);

CREATE TABLE order_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER NOT NULL,
  item_id TEXT NOT NULL,
  amount INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders (id),
  FOREIGN KEY (item_id) REFERENCES items (uid)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  source_id INTEGER,
  order_date TEXT,
  request_date TEXT,
  reference TEXT,
  reference_extra TEXT,
  order_status TEXT,
  notes TEXT,
  shipping_notes TEXT,
  picking_notes TEXT,
  warehouse_id INTEGER,
  ship_to TEXT,
  bill_to TEXT,
  shipment_id INTEGER,
  total_amount REAL,
  total_discount REAL,
  total_tax REAL,
  total_surcharge REAL,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (warehouse_id) REFERENCES warehouses (id),
  FOREIGN KEY (shipment_id) REFERENCES shipments (id)
);

CREATE TABLE shipment_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  shipment_id INTEGER NOT NULL,
  item_id TEXT NOT NULL,
  amount INTEGER NOT NULL,
  FOREIGN KEY (shipment_id) REFERENCES shipments (id),
  FOREIGN KEY (item_id) REFERENCES items (uid)
);

CREATE TABLE shipments (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  source_id INTEGER,
  order_date TEXT,
  request_date TEXT,
  shipment_date TEXT,
  shipment_type TEXT,
  shipment_status TEXT,
  notes TEXT,
  carrier_code TEXT,
  carrier_description TEXT,
  service_code TEXT,
  payment_type TEXT,
  transfer_mode TEXT,
  total_package_count INTEGER,
  total_package_weight REAL,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (order_id) REFERENCES orders (id)
);

CREATE TABLE suppliers (
  id INTEGER PRIMARY KEY,
  code TEXT,
  name TEXT,
  address TEXT,
  address_extra TEXT,
  city TEXT,
  zip_code TEXT,
  province TEXT,
  country TEXT,
  contact_name TEXT,
  phonenumber TEXT,
  reference TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE transfer_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  transfer_id INTEGER NOT NULL,
  item_id TEXT NOT NULL,
  amount INTEGER NOT NULL,
  FOREIGN KEY (transfer_id) REFERENCES transfers (id),
  FOREIGN KEY (item_id) REFERENCES items (uid)
);

CREATE TABLE transfers (
  id INTEGER PRIMARY KEY,
  reference TEXT,
  transfer_from INTEGER,
  transfer_to INTEGER,
  transfer_status TEXT,
  created_at TEXT,
  updated_at TEXT,
  FOREIGN KEY (transfer_from) REFERENCES warehouses (id),
  FOREIGN KEY (transfer_to) REFERENCES warehouses (id)
);

CREATE TABLE warehouses (
  id INTEGER PRIMARY KEY,
  code TEXT,
  name TEXT,
  address TEXT,
  zip TEXT,
  city TEXT,
  province TEXT,
  country TEXT,
  created_at TEXT,
  updated_at TEXT
);
