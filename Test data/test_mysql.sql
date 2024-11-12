DELETE FROM clients;  -- Replace `table_name` with each table name in the database
DELETE FROM contacts;
DELETE FROM inventories;
DELETE FROM inventory_locations;
DELETE FROM item_groups;
DELETE FROM item_line;
DELETE FROM item_types;
DELETE FROM items;
DELETE FROM locations;
DELETE FROM order_items;
DELETE FROM orders;
DELETE FROM shipment_items;
DELETE FROM shipments;
DELETE FROM sqlite_sequence;  -- This resets any AUTOINCREMENT counters
DELETE FROM suppliers;
DELETE FROM transfer_items;
DELETE FROM transfers;
DELETE FROM warehouses;