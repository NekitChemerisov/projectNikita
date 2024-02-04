# TaskManagerApp.py
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime
import sys

sys.path.append('C:/Users/cheme/OneDrive/Документы/python/projectNikita/project3/controller')
from TaskController import TaskController

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.task_controller = TaskController()

        self.task_name_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=5)

        self.task_list_treeview = ttk.Treeview(self.root, columns=("Name", "Priority", "Due Date"), show="headings")
        self.task_list_treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')
        self.task_list_treeview.heading("Name", text="Task Name")
        self.task_list_treeview.heading("Priority", text="Priority")
        self.task_list_treeview.heading("Due Date", text="Due Date")


    def add_task(self):
        name = self.task_name_var.get()
        priority = self.priority_var.get()
        due_date = self.due_date_var.get()
        if name and priority and due_date:
            self.task_controller.add_task(name, priority, due_date) 
            self.load_tasks()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def delete_task(self):
        selected_item = self.task_list_treeview.selection()
        if selected_item:
            task_id = self.task_list_treeview.item(selected_item)['values'][0]
            self.task_controller.delete_task(task_id) 
            self.load_tasks()

    def clear_tasks(self):
        self.task_controller.clear_tasks() 
        self.load_tasks()

    def load_tasks(self):
        name = "user"
        for i in self.task_list_treeview.get_children():
            self.task_list_treeview.delete(i)
        tasks = self.task_controller.get_tasks(name)
        for task in tasks:
            self.task_list_treeview.insert("", tk.END, values=(task.id, task.name, task.priority, task.due_date))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
