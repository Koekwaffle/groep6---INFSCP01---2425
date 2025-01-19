import sqlite3


def init():
    pass


def fetch_generic(table_name):
    con = sqlite3.connect('ILY_TEST.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    data = cur.fetchall()
    # print(data)
    return data


def fetch_by_id(table_name, id):
    con = sqlite3.connect('ILY_TEST.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
    data = cur.fetchall()
    # print(data)
    return data


def fetch_by_table_and_column(table_name, column_name, value):
    con = sqlite3.connect('ILY_TEST.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE {column_name} = ?", (value,))
    data = cur.fetchall()
    # print(data)
    return data

def execute_query(query, params=()):
    con = sqlite3.connect('ILY_TEST.db')
    cur = con.cursor()
    try:
        cur.execute(query, params)
        con.commit()
        return cur
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        con.close()

def get_connection():
    return sqlite3.connect('ILY_TEST.db')
