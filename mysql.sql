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
CREATE TABLE contacts_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    warehouse_id INTEGER NOT NULL,
    name TEXT,
    phone TEXT,
    email TEXT,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
);

-- Step 2: Copy data from the old table to the new table
INSERT INTO contacts_new (id, warehouse_id, name, phone, email)
SELECT id, warehouse_id, name, phone, email FROM contacts;

-- Step 3: Drop the original table
DROP TABLE contacts;

-- Step 4: Rename the new table to the original table name
ALTER TABLE contacts_new RENAME TO contacts;
