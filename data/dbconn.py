import sqlite3
import os

def get_db_connection():
    # Get the absolute path to the project root folder dynamically
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    db_path = os.path.join(project_root, 'ILY.db')
    
    conn = sqlite3.connect(db_path)
    return conn
