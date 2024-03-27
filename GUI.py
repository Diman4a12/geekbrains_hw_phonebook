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
    ttk.Button(frame, text="Добавить", command=lambda: add_subsriber((name.get(), surname.get(), phone_1.get(), phone_2.get(), date_birth.get(), email.get()))).pack(anchor=NW)
    ttk.Button(frame, text="Закрыть", command=add_phone.destroy).pack(anchor=NW)
    


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
    
    

frm = ttk.Frame(root, padding=10)
frm.grid()
columns = ("id", "name", "surname", "phone 1", "phone 2", "date birth", "email")
tree = ttk.Treeview(frm, columns=columns, show="headings")
tree.grid(columnspan=5, row=0)
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
for pers in show_all():
    tree.insert("", END, values=pers)
ttk.Button(frm, text="Добавить", command=create_entry).grid(column=0, row=10)
ttk.Button(frm, text="Выбрать", command=choose_row).grid(column=1, row=10)
ttk.Button(frm, text="Изменить", command=change_entry).grid(column=2, row=10)
ttk.Button(frm, text="Удалить", command=del_entry).grid(column=3, row=10)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=4, row=10)

#click_row = tree.item(tree.focus(), 'values')

selected = tree.focus()
temp = tree.item(selected, 'values')
print(temp)



def select_item():
    selected = tree.focus()
    temp = tree.item(selected, 'values')
    return temp