import tkinter as tk
from tkinter import ttk

def show_selected():
    selected_item = combobox.get()
    label.config(text=f"Ура, ты выбрал вариант: {selected_item}")

root = tk.Tk()
root.geometry('400x300')
root.title("Tkinter Интерфейс")

items = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4"]

listbox = tk.Listbox(root)
listbox.pack(pady=10)
for item in items:
    listbox.insert(tk.END, item)

combobox = ttk.Combobox(root, values=items)
combobox.pack(pady=10)

btn = tk.Button(root, text="Показать выбранный элемент", command=show_selected)
btn.pack(pady=10)

label = tk.Label(root, text="Выберите элемент из списка")
label.pack(pady=10)

root.mainloop()
