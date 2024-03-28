import sqlite3 as sq


conn = sq.connect("phonebook.db")

cur = conn.cursor()

cur.execute(
    """
             CREATE TABLE IF NOT EXISTS phonebook
             (
             id INTEGER PRIMARY KEY,
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
    

def update_subsriber(args, id):  
    conn = sq.connect("phonebook.db")
    cur = conn.cursor() 
    sql_query = """UPDATE phonebook SET
                    name = ?,
                    surname = ?,
                    phone_1 = ?,
                    phone_2 = ?,
                    date_birth = ?,
                    email = ?
                    WHERE id = ? """
    data = (args[0], args[1], args[2], args[3], args[4], args[5], id)
    cur.execute(sql_query, data)
    conn.commit()
    conn.close()
    
    
def find_subsriber(name="%", surname="%"):
    conn = sq.connect("phonebook.db")
    cur = conn.cursor()
    sql_query = "SELECT * FROM phonebook WHERE name LIKE ? AND surname LIKE ?"
    name += '%'
    surname += '%'    
    data = (name, surname)
    cur.execute(sql_query, data)
    users = cur.fetchall()
    conn.commit()
    conn.close()
    return users


conn.commit()
conn.close()
