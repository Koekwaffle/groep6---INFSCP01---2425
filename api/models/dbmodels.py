import sqlite3
import sys
import os

# Add the path where dbconn.py is located (just the directory, not the file)
sys.path.append(r'C:\Users\ronan\Documents\GitHub\groep6---INFSCP01---2425\data')

# Now you can import get_db_connection from dbconn
from dbconn import get_db_connection

def create_clients_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create the clients table
    cursor.execute('''
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
        updated_at TEXT
    );
    ''')
    
    conn.commit()
    conn.close()


def create_inventories_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create the inventories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventories (
        id INTEGER PRIMARY KEY,
        item_id TEXT,
        description TEXT,
        item_reference TEXT,
        locations TEXT, -- Consider storing locations as a JSON or CSV string
        total_on_hand INTEGER,
        total_expected INTEGER,
        total_ordered INTEGER,
        total_allocated INTEGER,
        total_available INTEGER,
        created_at TEXT,
        updated_at TEXT
    );
    ''')
    
    conn.commit()
    conn.close()


def create_item_groups_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the item_groups table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS item_groups (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')
    
    conn.commit()
    conn.close()


def create_item_line_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the item_line table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS item_line (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')
    
    conn.commit()
    conn.close()


def create_item_types_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the item_types table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS item_types (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')
    
    conn.commit()
    conn.close()


def create_items_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the items table
    cursor.execute('''
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
    ''')

    conn.commit()
    conn.close()


def create_locations_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the locations table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY,
        warehouse_id INTEGER,
        code TEXT,
        name TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')

    conn.commit()
    conn.close()


def create_orders_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the orders table
    cursor.execute('''
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
        warehouse_id INTEGER,
        ship_to TEXT,
        bill_to TEXT,
        shipment_id INTEGER,
        total_amount REAL,
        total_discount REAL,
        total_tax REAL,
        total_surcharge REAL,
        created_at TEXT,
        updated_at TEXT
    );
    ''')

    conn.commit()
    conn.close()


def create_shipments_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the shipments table
    cursor.execute('''
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
        updated_at TEXT
    );
    ''')

    conn.commit()
    conn.close()


def create_suppliers_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the suppliers table
    cursor.execute('''
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
    ''')

    conn.commit()
    conn.close()


def create_transfers_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the transfers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transfers (
        id INTEGER PRIMARY KEY,
        reference TEXT,
        transfer_from INTEGER,
        transfer_to INTEGER,
        transfer_status TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')

    conn.commit()
    conn.close()


def create_warehouses_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the warehouses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS warehouses (
        id INTEGER PRIMARY KEY,
        code TEXT,
        name TEXT,
        address TEXT,
        zip TEXT,
        city TEXT,
        province TEXT,
        country TEXT,
        contact_name TEXT,
        contact_phone TEXT,
        contact_email TEXT,
        created_at TEXT,
        updated_at TEXT
    );
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_clients_table()
    create_inventories_table()
    create_item_groups_table()
    create_item_line_table()
    create_item_types_table()
    create_items_table()
    create_locations_table()
    create_orders_table()
    create_shipments_table()
    create_suppliers_table()
    create_transfers_table()
    create_warehouses_table()
