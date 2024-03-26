from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Телефонный справочник')
root.geometry('500x500')


def create_entry():
    add_phone = Tk()
    add_phone.title('Добавить абонента')
    add_phone.geometry('400x400')
    frame = ttk.Frame(add_phone, padding=[8, 10])
    frame.grid()
    ttk.Label(frame, text="Введите имя").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Label(frame, text="Введите фамилию").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Label(frame, text="Введите номер телефона 1").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Label(frame, text="Введите номер телефона 2").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Label(frame, text="Дату рождения").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Label(frame, text="E-mail").pack(anchor=NW)
    entry = ttk.Entry(frame).pack(anchor=NW)
    ttk.Button(frame, text="Добавить").pack(anchor=NW)
    return frame


def change_entry():
    change_phone = Tk()
    change_phone.title('Изменить запись')
    change_phone.geometry('400x400')
    frame = ttk.Frame(change_phone, padding=[8, 10])
    frame.grid()
    ttk.Button(frame, text="Сохранить").pack(anchor=NW)
    return frame

def del_entry():
    del_phone = Tk()
    del_phone.title('Удалить запись')
    del_phone.geometry('210x80')
    frame = ttk.Frame(del_phone, padding=[8, 10])
    frame.grid()
    ttk.Label(frame, text="Вы действительно хотите удалить?").pack(anchor=CENTER)
    ttk.Button(frame, text="Удалить").pack(anchor=CENTER)
    return frame





frm = ttk.Frame(root, padding=10)
frm.grid()
columns = ('name', 'surname', 'phone 1', 'phone 2', 'date birth', 'email')
tree = ttk.Treeview(frm, columns=columns, show='headings').grid(column=1, row=0)
#tree.heading('name', text='Имя')
#tree.heading('surname', text='Имя')
#tree.heading('phone 1', text='Имя')
#tree.heading('phone 2', text='Имя')
#tree.heading('date birth', text='Имя')
#tree.heading('email', text='Имя')
ttk.Button(frm, text="Добавить", command=create_entry).grid(column=1, row=10)
ttk.Button(frm, text="Выбрать").grid(column=2, row=10)
ttk.Button(frm, text="Изменить", command=change_entry).grid(column=3, row=10)
ttk.Button(frm, text="Удалить", command=del_entry).grid(column=4, row=10)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=5, row=10)
