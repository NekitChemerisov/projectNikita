import tkinter as tk

def show_message():
    label["text"] = entry.get()     # получаем введенный текст

def clean():
    label["text"] = ""
 
root = tk.Tk()
root.geometry("250x200") 
 
entry = tk.Entry()
entry.pack()
  
btn = tk.Button(text="Print", command=show_message)
btn.pack()

btn2 = tk.Button(text="Clean", command=clean)
btn2.pack()
 
label = tk.Label()
label.pack()

root.bind('<Return>', lambda event: clean()) 
root.mainloop()