import sqlite3
import os

def get_db_connection():
    # Get the absolute path to the project root folder dynamically
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Define the path for the database file relative to the project root
    db_path = os.path.join(project_root, 'database.db')
    
    conn = sqlite3.connect(db_path)
    return conn
