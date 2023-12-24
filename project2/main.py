import tkinter as tk
from tkinter import Menu, Entry, Label, Button, Listbox, filedialog, messagebox
import task_manager
from storage import Storage

storage = Storage("bd.txt")

def add_task():
    task_name = entry_task_name.get()
    date = entry_date.get()
    description = entry_description.get()
    task = task_manager.Task(task_name, date, description, "Новая")
    storage.add_task(task)
    refresh_tasks()

def delete_task():
    selected_task = listbox_tasks.get(listbox_tasks.curselection())
    task_name = selected_task.split(' - ')[0]
    storage.delete_task(task_name)
    refresh_tasks()

def refresh_tasks():
    listbox_tasks.delete(0, tk.END)
    for task in storage.get_all_tasks():
        listbox_tasks.insert(tk.END, format_task_string(task))

def clear_fields():
    entry_task_name.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def format_task_string(task):
    return f"{task.task_name} [Дата: {task.date}] - {task.description}"

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        storage.file_path = filepath
        refresh_tasks()

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        storage.file_path = filepath
        storage.save_tasks()

def exit_app():
    window.quit()

def create_main_window():
    global window, entry_task_name, entry_date, entry_description, listbox_tasks

    window = tk.Tk()
    window.title("Задачник")
    window.geometry("800x600")

    menu = Menu(window)
    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label="Открыть...", command=open_file)
    file_menu.add_command(label="Сохранить...", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=exit_app)
    menu.add_cascade(label="Файл", menu=file_menu)
    window.config(menu=menu)

    Label(window, text="Имя задачи:").pack()
    entry_task_name = Entry(window)
    entry_task_name.pack()

    Label(window, text="Дата:").pack()
    entry_date = Entry(window)
    entry_date.pack()

    Label(window, text="Описание:").pack()
    entry_description = Entry(window)
    entry_description.pack()

    Button(window, text="Добавить задачу", command=add_task).pack()
    Button(window, text="Удалить выбранную задачу", command=delete_task).pack()
    Button(window, text="Очистить поля", command=clear_fields).pack()

    listbox_tasks = Listbox(window)
    listbox_tasks.pack(fill=tk.BOTH, expand=True)
    refresh_tasks()

    window.mainloop()

create_main_window()
