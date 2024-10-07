import sqlite3
import os

def get_db_connection():
    # Path to where your database file will be stored
    db_path = r'C:\Users\ronan\Documents\GitHub\groep6---INFSCP01---2425\database.db'
    conn = sqlite3.connect(db_path)
    return conn
