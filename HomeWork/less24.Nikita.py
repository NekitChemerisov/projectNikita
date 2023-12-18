#2
'''import tkinter as tk
from tkinter import messagebox

def show_selected():
    selected = []
    if var.get() == 1:
        selected.append('Да')
    if var1.get() == 1:
        selected.append('Нет')
    messagebox.showinfo("Выбор", "Выбрано: " + ', '.join(selected))

root = tk.Tk()
root.geometry('400x300')
root.title("Tkinter Интерфейс")

frame1 = tk.Frame(root)
frame1.pack(pady=10)

var = tk.IntVar()
var1 = tk.IntVar()

checkButton = tk.Checkbutton(frame1, text='Да', variable=var, onvalue=1, offvalue=0)
checkButton.pack(side=tk.LEFT)
checkButton1 = tk.Checkbutton(frame1, text='Нет', variable=var1, onvalue=1, offvalue=0)
checkButton1.pack(side=tk.LEFT)

btn = tk.Button(root, text="Показать выбранный элемент", command=show_selected)
btn.pack(pady=10)

root.mainloop()'''

#3
import tkinter as tk
from tkinter import font

def update_interface():
    if bold_var.get() == 1:
        label.config(font=("Helvetica", 12, "bold"))
    else:
        label.config(font=("Helvetica", 12, "normal"))

    if red_var.get() == 1:
        label.config(fg="red")
    else:
        label.config(fg="black")

root = tk.Tk()
root.geometry('400x300')
root.title("Продвинутый интерфейс Tkinter")

bold_var = tk.IntVar()
red_var = tk.IntVar()

bold_check = tk.Checkbutton(root, text='Жирный', variable=bold_var, onvalue=1, offvalue=0, command=update_interface)
bold_check.pack()

red_check = tk.Checkbutton(root, text='Красный', variable=red_var, onvalue=1, offvalue=0, command=update_interface)
red_check.pack()

label = tk.Label(root, text="Текст от студента Каздев", font=("Helvetica", 12))
label.pack()

root.mainloop()

