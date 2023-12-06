import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.title("Для лекции 21")

def one_button_click(event):
    entry = tk.Entry()
    entry.pack()

    btn = tk.Button(text="Save")
    btn.pack()

root.bind("<Button-1>", one_button_click)

root.mainloop()