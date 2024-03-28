from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from database import *
import json

root = Tk()
root.title("Телефонный справочник")
root.geometry("810x400")


def update_table():
    items = tree.get_children()
    for elemet in items:
        tree.delete(elemet)
    for pers in show_all():
        tree.insert("", END, values=pers)


def update_find_table(tree1, name, surname):
    items = tree1.get_children()
    for elemet in items:
        tree1.delete(elemet)
    item = find_subsriber(name, surname)
    for pers in item:
        tree1.insert("", END, values=pers)


def create_entry():
    add_phone = Tk()
    add_phone.title("Добавить абонента")
    add_phone.geometry("400x400")
    frame = ttk.Frame(add_phone, padding=[8, 10])
    frame.grid()
    ttk.Label(frame, text="Введите имя").pack(anchor=NW)
    name = ttk.Entry(frame)
    name.pack(anchor=NW)
    ttk.Label(frame, text="Введите фамилию").pack(anchor=NW)
    surname = ttk.Entry(frame)
    surname.pack(anchor=NW)
    ttk.Label(frame, text="Введите номер телефона 1").pack(anchor=NW)
    phone_1 = ttk.Entry(frame)
    phone_1.pack(anchor=NW)
    ttk.Label(frame, text="Введите номер телефона 2").pack(anchor=NW)
    phone_2 = ttk.Entry(frame)
    phone_2.pack(anchor=NW)
    ttk.Label(frame, text="Дату рождения").pack(anchor=NW)
    date_birth = ttk.Entry(frame)
    date_birth.pack(anchor=NW)
    ttk.Label(frame, text="E-mail").pack(anchor=NW)
    email = ttk.Entry(frame)
    email.pack(anchor=NW)
    ttk.Button(
        frame,
        text="Добавить",
        command=lambda: (
            add_subsriber(
                (
                    name.get(),
                    surname.get(),
                    phone_1.get(),
                    phone_2.get(),
                    date_birth.get(),
                    email.get(),
                )
            ),
            update_table(),
        ),
    ).pack(anchor=NW)
    ttk.Button(frame, text="Закрыть", command=add_phone.destroy).pack(anchor=NW)


def change_entry():
    change_phone = Tk()
    change_phone.title("Изменить запись")
    change_phone.geometry("400x400")
    frame = ttk.Frame(change_phone, padding=[8, 10])
    frame.grid()
    id = select_item()
    ttk.Label(frame, text="Имя").pack(anchor=NW)
    name = ttk.Entry(frame)
    name.insert(0, id[1])
    name.pack(anchor=NW)
    ttk.Label(frame, text="Фамилию").pack(anchor=NW)
    surname = ttk.Entry(frame)
    surname.insert(0, id[2])
    surname.pack(anchor=NW)
    ttk.Label(frame, text="Номер телефона 1").pack(anchor=NW)
    phone_1 = ttk.Entry(frame)
    phone_1.insert(0, id[3])
    phone_1.pack(anchor=NW)
    ttk.Label(frame, text="Номер телефона 2").pack(anchor=NW)
    phone_2 = ttk.Entry(frame)
    phone_2.insert(0, id[4])
    phone_2.pack(anchor=NW)
    ttk.Label(frame, text="Дата рождения").pack(anchor=NW)
    date_birth = ttk.Entry(frame)
    date_birth.insert(0, id[5])
    date_birth.pack(anchor=NW)
    ttk.Label(frame, text="E-mail").pack(anchor=NW)
    email = ttk.Entry(frame)
    email.insert(0, id[6])
    email.pack(anchor=NW)
    ttk.Button(
        frame,
        text="Сохранить",
        command=lambda: (
            update_subsriber(
                (
                    name.get(),
                    surname.get(),
                    phone_1.get(),
                    phone_2.get(),
                    date_birth.get(),
                    email.get(),
                ),
                id[0],
            ),
            update_table(),
        ),
    ).pack(anchor=NW)
    ttk.Button(frame, text="Закрыть", command=change_phone.destroy).pack(anchor=NW)


def del_entry():
    del_phone = Tk()
    del_phone.title("Удалить запись")
    del_phone.geometry("310x110")
    frame = ttk.Frame(del_phone, padding=[8, 10])
    frame.grid()
    id = select_item()
    ttk.Label(frame, text=f"Вы действительно хотите удалить контакнт {id[1]}?").pack(
        anchor=CENTER
    )
    ttk.Button(
        frame,
        text="Удалить",
        command=lambda: (del_subsriber(id[0]), update_table(), del_phone.destroy()),
    ).pack(anchor=CENTER)


def choose_row():
    choose = Tk()
    choose.title("Показать запись")
    choose.geometry("210x250")
    id = select_item()
    ttk.Label(choose, text=f"Имя: {id[1]}").pack(anchor=NW)
    ttk.Label(choose, text=f"Фамилия: {id[2]}").pack(anchor=NW)
    ttk.Label(choose, text=f"Телефон 1: {id[3]}").pack(anchor=NW)
    ttk.Label(choose, text=f"Телефон 2: {id[4]}").pack(anchor=NW)
    ttk.Label(choose, text=f"Дата рождения: {id[5]}").pack(anchor=NW)
    ttk.Label(choose, text=f"E-mail: {id[6]}").pack(anchor=NW)
    ttk.Button(choose, text="Выход", command=choose.destroy).pack(anchor=NW)


def find_row():

    find = Tk()
    find.title("Найти абонента")
    find.geometry("810x400")
    frame = ttk.Frame(find, padding=[8, 10])
    frame.grid()
    ttk.Label(frame, text="Введите имя").grid(column=1, row=0)
    name = ttk.Entry(frame)
    name.grid(column=2, row=0)
    ttk.Label(frame, text="Введите фамилию").grid(column=3, row=0)
    surname = ttk.Entry(frame)
    surname.grid(column=4, row=0)
    btn_faind = ttk.Button(
        frame,
        text="Найти",
        command=lambda: update_find_table(tree1, name.get(), surname.get()),
    )
    btn_faind.grid(column=5, row=0)
    columns = ("id", "name", "surname", "phone 1", "phone 2", "date birth", "email")
    tree1 = ttk.Treeview(frame, columns=columns, show="headings")
    tree1.grid(columnspan=6, row=1)
    find.grid_columnconfigure(0, weight=1)
    tree1.heading("id", text="№")
    tree1.heading("name", text="Имя")
    tree1.heading("surname", text="Фамилия")
    tree1.heading("phone 1", text="Телефон 1")
    tree1.heading("phone 2", text="Телефон 2")
    tree1.heading("date birth", text="Дата рождения")
    tree1.heading("email", text="E-mail")
    tree1.column("#1", stretch=NO, width=20)
    tree1.column("#2", stretch=NO, width=110)
    tree1.column("#3", stretch=NO, width=110)
    tree1.column("#4", stretch=NO, width=110)
    tree1.column("#5", stretch=NO, width=110)
    tree1.column("#6", stretch=NO, width=110)
    tree1.column("#6", stretch=NO, width=110)
    sb1 = Scrollbar(frame, orient=VERTICAL)
    sb1.grid(column=6, row=1, sticky="ns")
    tree1.config(yscrollcommand=sb1.set)
    sb1.config(command=tree1.yview)
    ttk.Button(frame, text="Выход", command=find.destroy).grid(column=3, row=6)


def import_contact():
    file_read = filedialog.askopenfilename()
    with open(file_read, "r") as file:
        contacts_js = file.read()
        contacts = json.loads(contacts_js)
        for item in contacts:
            add_subsriber(
                (
                    item["First Name"],
                    item["Last Name"],
                    item["Mobile Phone"],
                    item["Home Phone"],
                    item["Birthday"],
                    item["E-mail Address"],
                )
            )
            update_table()


frm = ttk.Frame(root, padding=10)
frm.grid()
columns = ("id", "name", "surname", "phone 1", "phone 2", "date birth", "email")
tree = ttk.Treeview(frm, columns=columns, show="headings")
tree.grid(columnspan=7, row=1)
root.grid_columnconfigure(0, weight=1)
tree.heading("id", text="№")
tree.heading("name", text="Имя")
tree.heading("surname", text="Фамилия")
tree.heading("phone 1", text="Телефон 1")
tree.heading("phone 2", text="Телефон 2")
tree.heading("date birth", text="Дата рождения")
tree.heading("email", text="E-mail")
tree.column("#1", stretch=NO, width=20)
tree.column("#2", stretch=NO, width=110)
tree.column("#3", stretch=NO, width=110)
tree.column("#4", stretch=NO, width=110)
tree.column("#5", stretch=NO, width=110)
tree.column("#6", stretch=NO, width=110)
tree.column("#6", stretch=NO, width=110)
sb = Scrollbar(frm, orient=VERTICAL)
sb.grid(column=7, row=1, sticky="ns")
tree.config(yscrollcommand=sb.set)
sb.config(command=tree.yview)
update_table()
ttk.Button(frm, text="Добавить", command=create_entry).grid(column=0, row=12)
ttk.Button(frm, text="Выбрать", command=choose_row).grid(column=1, row=12)
ttk.Button(frm, text="Найти", command=find_row).grid(column=2, row=12)
ttk.Button(frm, text="Изменить", command=change_entry).grid(column=3, row=12)
ttk.Button(frm, text="Импортировать", command=import_contact).grid(column=4, row=12)
ttk.Button(frm, text="Удалить", command=del_entry).grid(column=5, row=12)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=6, row=12)


def select_item():
    selected = tree.focus()
    temp = tree.item(selected, "values")
    return temp
