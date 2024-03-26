import sqlite3 as sq


conn = sq.connect("phonebook.db")

cur = conn.cursor()

cur.execute(
    """
             CREATE TABLE IF NOT EXISTS users
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
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users


def add_subsriber(**args):
    cur.execute(
        "INSERT INTO users (name, surname, phone_1, phone_2, date_birth, email) VALUES (?, ?, ?)",
        args,
    )


conn.commit()
conn.close()
