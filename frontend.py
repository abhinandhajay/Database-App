from tkinter import *
from backend import Database

database = Database()

def get_selected_row(event):
    try:
        global selection
        index = list1.curselection()[0]
        selection = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selection[1])
        e2.delete(0,END)
        e2.insert(END,selection[2])
        e3.delete(0,END)
        e3.insert(END,selection[3])
        e4.delete(0,END)
        e4.insert(END,selection[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    list1.delete(0,END)
    database.delete(selection[0])
    view_command()

def update_command():
    list1.delete(0,END)
    database.update(selection[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

window = Tk()

window.wm_title("Bookstore")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 10, width = 30)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 10)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = insert_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete Selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

view_command()

window.mainloop()
