import sqlite3 as sq


conn = sq.connect("phonebook.db")

cur = conn.cursor()

cur.execute(
    """
             CREATE TABLE IF NOT EXISTS users
             (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             surname TEXT,
             phone 1 TEXT,
             phone 2 TEXT,
             date birth TEXT,
             email TEXT
             );
             """
)
