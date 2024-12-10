import sqlite3
import json

class db_start:
    def create_database(self):
        try:
            # SQLite creates the database file automatically when connecting if it doesn't exist
            database_name = "Cargohub_db.sqlite"
            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()

            # Define the table creation SQL statements
            create_table_clients = """
            CREATE TABLE IF NOT EXISTS clients (
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
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_inventory = """
            CREATE TABLE IF NOT EXISTS inventories (
                id INTEGER PRIMARY KEY,
                item_id TEXT,
                description TEXT,
                item_reference TEXT,
                locations TEXT,
                total_on_hand INTEGER,
                total_expected INTEGER,
                total_ordered INTEGER,
                total_allocated INTEGER,
                total_available INTEGER,
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_items = """
            CREATE TABLE IF NOT EXISTS items (
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
                updated_at TEXT
            );
            """

            create_table_locations = """
            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY,
                warehouse_id INTEGER,
                code TEXT,
                name TEXT,
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_orders = """
            CREATE TABLE IF NOT EXISTS orders (
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
                warehouse_id INTEGERL,
                ship_to TEXT,
                bill_to TEXT,
                shipment_id INTEGER,
                total_amount REAL,
                total_discount REAL,
                total_tax REAL,
                total_surcharge REAL,
                created_at TEXT,
                updated_at TEXT,
                items TEXT
            );
            """

            create_table_shipments = """
            CREATE TABLE IF NOT EXISTS shipments (
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
                items TEXT
            );
            """

            create_table_suppliers = """
            CREATE TABLE IF NOT EXISTS suppliers (
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
            """

            create_table_transfers = """
            CREATE TABLE IF NOT EXISTS transfers (
                id INTEGER PRIMARY KEY,
                reference TEXT,
                transfer_from TEXT,
                transfer_to INTEGER,
                transfer_status TEXT,
                created_at TEXT,
                updated_at TEXT,
                items TEXT
            );
            """

            create_table_warehouses = """
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY,
                code TEXT,
                name TEXT,
                address TEXT,
                zip TEXT,
                city TEXT,
                province TEXT,
                country TEXT,
                contact TEXT,
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_item_groups = """
            CREATE TABLE IF NOT EXISTS item_groups (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_item_lines = """
            CREATE TABLE IF NOT EXISTS item_lines (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                created_at TEXT,
                updated_at TEXT
            );
            """

            create_table_item_types = """
            CREATE TABLE IF NOT EXISTS item_types (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                created_at TEXT,
                updated_at TEXT
            );
            """

            # Execute all table creation queries
            cursor.execute(create_table_clients)
            cursor.execute(create_table_inventory)
            cursor.execute(create_table_items)
            cursor.execute(create_table_locations)
            cursor.execute(create_table_orders)
            cursor.execute(create_table_shipments)
            cursor.execute(create_table_suppliers)
            cursor.execute(create_table_transfers)
            cursor.execute(create_table_warehouses)
            cursor.execute(create_table_item_groups)
            cursor.execute(create_table_item_lines)
            cursor.execute(create_table_item_types)

            conn.commit()
            cursor.close()
            conn.close()
            print("Database and tables created successfully.")
        except sqlite3.Error as error:
            print(f"Error creating database or tables: {error}")

    def connection(self, database_name):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except sqlite3.Error as error:
            print(f"Error connecting to database {database_name}: {error}")
            return None
