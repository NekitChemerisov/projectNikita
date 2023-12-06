import tkinter as tk

window = tk.Tk()
window.title("Анкета участника")
window.geometry("300x400")

label = tk.Label(window, text = "Меня зовут Наруто Удзумаки, мой друг Учиха Саске, нам 12 лет!")
label.pack()

label.mainloop()