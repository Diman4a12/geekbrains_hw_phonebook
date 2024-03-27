from tkinter import *
from tkinter import ttk
from database import *

root = Tk()
root.title("Телефонный справочник")
root.geometry("800x400")


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
    list_add = (name.get(), surname.get(), phone_1.get(), phone_2.get(), date_birth.get(), email.get())
    ttk.Button(frame, text="Добавить", command=add_subsriber(list_add)).pack(anchor=NW)
    ttk.Button(frame, text="Закрыть", command=add_phone.destroy).pack(anchor=NW)
    #return frame


def change_entry():
    change_phone = Tk()
    change_phone.title("Изменить запись")
    change_phone.geometry("400x400")
    frame = ttk.Frame(change_phone, padding=[8, 10])
    frame.grid()
    ttk.Button(frame, text="Сохранить").pack(anchor=NW)
    return frame


def del_entry():
    del_phone = Tk()
    del_phone.title("Удалить запись")
    del_phone.geometry("210x80")
    frame = ttk.Frame(del_phone, padding=[8, 10])
    frame.grid()
    ttk.Label(frame, text="Вы действительно хотите удалить?").pack(anchor=CENTER)
    ttk.Button(frame, text="Удалить").pack(anchor=CENTER)
    return frame


frm = ttk.Frame(root, padding=10)
frm.grid()
columns = ("name", "surname", "phone 1", "phone 2", "date birth", "email")
tree = ttk.Treeview(frm, columns=columns, show="headings")
tree.grid(columnspan=5, row=0)
root.grid_columnconfigure(0, weight=1)
tree.heading("name", text="Имя")
tree.heading("surname", text="Фамилия")
tree.heading("phone 1", text="Телефон 1")
tree.heading("phone 2", text="Телефон 2")
tree.heading("date birth", text="Дата рождения")
tree.heading("email", text="E-mail")
tree.column("#1", stretch=NO, width=130)
tree.column("#2", stretch=NO, width=130)
tree.column("#3", stretch=NO, width=130)
tree.column("#4", stretch=NO, width=130)
tree.column("#5", stretch=NO, width=130)
tree.column("#6", stretch=NO, width=130)
ttk.Button(frm, text="Добавить", command=create_entry).grid(column=0, row=10)
ttk.Button(frm, text="Выбрать").grid(column=1, row=10)
ttk.Button(frm, text="Изменить", command=change_entry).grid(column=2, row=10)
ttk.Button(frm, text="Удалить", command=del_entry).grid(column=3, row=10)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=4, row=10)
