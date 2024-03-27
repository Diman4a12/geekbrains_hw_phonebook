import sqlite3 as sq


conn = sq.connect("phonebook.db")

cur = conn.cursor()

cur.execute(
    """
             CREATE TABLE IF NOT EXISTS phonebook
             (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             surname TEXT,
             phone_1 TEXT NOT NULL,
             phone_2 TEXT,
             date_birth TEXT,
             email TEXT
             );
             """
)


def show_all():
    conn = sq.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    users = cur.fetchall()
    conn.commit()
    conn.close()
    return users


def add_subsriber(args):
    conn = sq.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook VALUES (NULL, ?, ?, ?, ?, ?, ?)",
        args,
    )
    conn.commit()
    conn.close()


def del_subsriber(id):
    conn = sq.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute(
        f"DELETE FROM phonebook WHERE id = {id}"
    )
    conn.commit()
    conn.close()
    
    
def find_subsriber(name, surname="NULL"):
    conn = sq.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM phonebook WHERE name = {name} AND surname = {surname}"
    )
    users = cur.fetchall()
    conn.commit()
    conn.close()
    #return users


conn.commit()
conn.close()
