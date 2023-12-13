import tkinter as tk

root = tk.Tk()
root.geometry('400x250')  
root.title("Для лекции 22")

def show_text():
    entered_text = text.get("1.0", "end-1c")
    label.config(text=f"{entered_text}")

def change_font():
    text.config(font=("Times New Roman", 12))

text = tk.Text(root, height=5, width=30)
text.pack()

btn_print = tk.Button(root, text="Print", command=show_text)
btn_print.pack()

btn_change_font = tk.Button(root, text="Change Font to Times New Roman", command=change_font)
btn_change_font.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
