-- CREATE TABLE IF NOT EXISTS shipment_items (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     shipment_id INTEGER NOT NULL,
--     item_id TEXT NOT NULL,
--     amount INTEGER NOT NULL,
--     FOREIGN KEY (shipment_id) REFERENCES shipments(id),
--     FOREIGN KEY (item_id) REFERENCES items(uid)
-- );

-- Table to store transfer information
-- CREATE TABLE IF NOT EXISTS transfers (
--     id INTEGER PRIMARY KEY,
--     reference TEXT,
--     transfer_from INTEGER, -- Assuming this could be linked to another table if needed
--     transfer_to INTEGER, -- Assuming this could be linked to another table if needed
--     transfer_status TEXT,
--     created_at TEXT,
--     updated_at TEXT
-- );

-- -- Table to store items related to each transfer
-- CREATE TABLE IF NOT EXISTS transfer_items (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     transfer_id INTEGER NOT NULL,
--     item_id TEXT NOT NULL,
--     amount INTEGER NOT NULL,
--     FOREIGN KEY (transfer_id) REFERENCES transfers(id),
--     FOREIGN KEY (item_id) REFERENCES items(uid)
-- );

-- DROP TABLE IF EXISTS warehouses;

-- CREATE TABLE IF NOT EXISTS warehouses (
--     id INTEGER PRIMARY KEY,
--     code TEXT,
--     name TEXT,
--     address TEXT,
--     zip TEXT,
--     city TEXT,
--     province TEXT,
--     country TEXT,
--     created_at TEXT,
--     updated_at TEXT
-- );

-- CREATE TABLE IF NOT EXISTS contacts (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     warehouse_id INTEGER NOT NULL,   -- Foreign key to link to the warehouse
--     name TEXT,
--     phone TEXT,
--     email TEXT,
--     created_at TEXT,
--     updated_at TEXT,
--     FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
-- );

-- Step 1: Create a new table without `created_at` and `updated_at`
-- CREATE TABLE contacts_new (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     warehouse_id INTEGER NOT NULL,
--     name TEXT,
--     phone TEXT,
--     email TEXT,
--     FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
-- );

-- -- Step 2: Copy data from the old table to the new table
-- INSERT INTO contacts_new (id, warehouse_id, name, phone, email)
-- SELECT id, warehouse_id, name, phone, email FROM contacts;

-- -- Step 3: Drop the original table
-- DROP TABLE contacts;

-- -- Step 4: Rename the new table to the original table name
-- ALTER TABLE contacts_new RENAME TO contacts;

-- CREATE TABLE inventories_new (
--     id INTEGER PRIMARY KEY,
--     item_id TEXT,
--     description TEXT,
--     item_reference TEXT,
--     location_id INTEGER,  -- New foreign key column to link to locations table
--     total_on_hand INTEGER,
--     total_expected INTEGER,
--     total_ordered INTEGER,
--     total_allocated INTEGER,
--     total_available INTEGER,
--     created_at TEXT,
--     updated_at TEXT,
--     FOREIGN KEY (location_id) REFERENCES locations(id)
-- );

-- INSERT INTO inventories_new (id, item_id, description, item_reference, total_on_hand, total_expected, total_ordered, total_allocated, total_available, created_at, updated_at)
-- SELECT id, item_id, description, item_reference, total_on_hand, total_expected, total_ordered, total_allocated, total_available, created_at, updated_at
-- FROM inventories;

-- DROP TABLE inventories;

-- ALTER TABLE inventories_new RENAME TO inventories;

-- CREATE TABLE IF NOT EXISTS inventory_locations (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     inventory_id INTEGER NOT NULL,  -- References an inventory item
--     location_id INTEGER NOT NULL,   -- References a location
--     FOREIGN KEY (inventory_id) REFERENCES inventories(id),
--     FOREIGN KEY (location_id) REFERENCES locations(id)
-- );
