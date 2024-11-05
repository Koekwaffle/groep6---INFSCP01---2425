import sqlite3


def init(table_name):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM " + table_name)
    data = cur.fetchall()
    # print(data)
    return data
