import tkinter as tk
root = tk.Tk()
root.title("Buttons & Display")

title_label=tk.Label(root,text="Hello,Tkinter",font=("Arial",18))
title_label.pack(pady=10)


name_label = tk.Label(root,text="Your name:")
name_label.pack()

name_entry = tk.Entry(root,width=25)
name_entry.pack(pady=5)



root.mainloop()

