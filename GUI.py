from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Телефонный справочник')
root.geometry('500x500')

def create_entry ():
    add_phone = Tk()
    add_phone.title('Добавить абонента')
    add_phone.geometry('400x400')
    frame = ttk.Frame(add_phone, padding=[8,10])
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
    ttk.Button(frame, text="Дбавить").pack(anchor=NW)
    return frame


frm = ttk.Frame(root, padding=[50, 450])
frm.grid()
ttk.Button(frm, text="Добавить", command=create_entry).grid(column=1, row=0)
ttk.Button(frm, text="Выбрать").grid(column=2, row=0)
ttk.Button(frm, text="Изменить").grid(column=3, row=0)
ttk.Button(frm, text="Удалить").grid(column=4, row=0)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=5, row=0)

#root.geometry('500x500')
#
#label = Label(text="Hello")
#label.pack()
