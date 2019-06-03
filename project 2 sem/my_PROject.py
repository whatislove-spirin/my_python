from tkinter import *
import json
from tkinter import messagebox as mb

lst = []
lst_delete = []

#functions----
def add():
    lst = [] 
    dictionary = {}
    dictionary["task"] = entry_task.get()
    dictionary["category"] = entry_category.get()
    dictionary['time'] = entry_time.get()
    lst.append(dictionary)
    writer(lst)
    entry_task.delete(0,END)
    entry_category.delete(0,END)
    entry_time.delete(0,END)

def show_list():
    text_list_of_tasks.configure(state=NORMAL)
    text_list_of_tasks.delete(1.0, END)
    try:
        button_ready_to_remove.place_forget()
        button_delete_frame2.place_forget()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)

    except:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + str(todo['task']) + " " + "Категория: " + str(todo[
                                                                                                          'category']) + " " + "Дата: " + str(
                todo['time']) + '\n')
            text_list_of_tasks.configure(state=DISABLED)
    text_list_of_tasks.configure(state=DISABLED)

def delete():
    for i in reversed(listbox_delete.curselection()):
        listbox_delete.delete(i)
        lst_delete.append(i)

def full_del():
    global lst_delete
    with open('todo_list.json', 'r', encoding='cp1251') as json_file:
        contents = json.load(json_file)
    for i in sorted(lst_delete, reverse=True):
        contents.pop(i)
    with open('todo_list.json', 'w') as file_output_json:
        json.dump(contents, file_output_json)
    lst_delete = []
    show_list()
    
def delete_task():
    try:
        global listbox_delete
        global button_delete_frame2
        listbox_delete.delete(0, END)
        button_delete_frame2.place(x=20, y=45)
        button_ready_to_remove.place(x=160, y=45)
        text_list_of_tasks.grid_remove()
        listbox_delete.grid(row=0, column=0, padx=1, pady=1)
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            listbox_delete.insert(END, "Задача: " + todo['task'] + " " + "Категория: " + todo['category'] + " " + "Дата: " +
                                todo['time'] + '\n') 
    except Exception as ex:
        print(ex)

def writer(input_text):
    try:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for i in input_text:
            contents.append(i)
    except Exception as ex:
        print(ex)
    try:
        with open('todo_list.json', 'w', encoding='windows-1251') as file_write:
            json.dump(contents, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)


def first_open_tasks():
    try:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)
    except:
        with open('todo_list.json', 'w', encoding='windows-1251') as file_write:
            json.dump([], file_write, sort_keys=False, ensure_ascii=False)

def exit1():
    root.destroy()
    
#main_frame-------
root = Tk()
root.title("Task manager")
root.geometry('648x212')

#colors----------------
main_bg_color="#30302F"
text_color="#F0ECE9"
button_text_color="#ffffff"
button_color="#DF5A00"
active_button="#FF6600"
#frames---------------
frame_inputs = Frame(root, width=320, height=320, background=main_bg_color)
frame_window = Frame(root, width=320, height=80, background=main_bg_color)

frame_buttons = Frame(root, width=320, height=75, background=main_bg_color)
frame_dell_buttons = Frame(root, width=330, height=137, background=main_bg_color)

frame_inputs.place(x=0, y=0)
frame_buttons.place(x=338, y=0)
frame_window.place(x=0, y=75)
frame_dell_buttons.place(x=338, y=75)

text_list_of_tasks = Text(frame_window, width=41, height=8)
text_list_of_tasks.grid(row=0, column=0, padx=3, pady=3)
text_list_of_tasks.configure(state=DISABLED)
#input fields------------------------------
label_task = Label(frame_inputs, text='Задача: ', fg=text_color, bg=main_bg_color)
label_task.grid(row=0, column=0, pady=2)

label_category = Label(frame_inputs, text='Категория: ', fg=text_color, bg=main_bg_color)
label_category.grid(row=1, column=0, pady=2)

label_time = Label(frame_inputs, text='Время: ', fg=text_color, width=12, bg=main_bg_color)
label_time.grid(row=2, column=0, pady=2)

entry_task = Entry(frame_inputs, width=40)
entry_task.grid(row=0, column=1, padx=2, pady=1)

entry_category = Entry(frame_inputs, width=40)
entry_category.grid(row=1, column=1)

entry_time = Entry(frame_inputs, width=40)
entry_time.grid(row=2, column=1)

#buttons------------------------
button_add = Button(frame_buttons, text="Добавить", width=18, command=add, bg=button_color, fg=button_text_color,
                    activebackground=active_button, relief='raised')
button_add.place(x=20, y=10)

button_delete = Button(frame_buttons, text="Удалить задачу", width=18, command=delete_task, bg=button_color, fg=button_text_color,
                       activebackground=active_button, relief='raised')
button_delete.place(x=20, y=40)

button_list_of_tasks = Button(frame_buttons, text="Список задач", width=18, command=show_list, bg=button_color, fg=button_text_color,
                              activebackground=active_button, relief='raised')
button_list_of_tasks.place(x=160, y=10)

button_exit = Button(frame_buttons, text="Выход", width=18, command=exit1, bg=button_color, fg=button_text_color,
                     activebackground=active_button, relief='raised')
button_exit.place(x=160, y=40)

button_delete_frame2 = Button(frame_dell_buttons, text='Удалить', width=18, activebackground=active_button, bg=button_color, fg=button_text_color,
                              command=delete)
button_delete_frame2.place(x=20, y=40)
button_delete_frame2.place_forget()

button_ready_to_remove = Button(frame_dell_buttons, text='Готово', width=18, activebackground=active_button, bg=button_color, fg=button_text_color,
                                command=full_del)
button_ready_to_remove.place(x=160, y=40)
button_ready_to_remove.place_forget()

listbox_delete = Listbox(frame_window, selectmode=MULTIPLE, width=53, highlightcolor='white', bg='white',
                         selectbackground=active_button)
listbox_delete.grid(row=0, column=0)
listbox_delete.grid_remove()

first_open_tasks()
root.resizable(width=False, height=False)
root.mainloop()
