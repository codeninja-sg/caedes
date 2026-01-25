import tkinter as tk

root=tk.Tk()
root.title("drawing Pad")
root.geometry("800x600")

root.title("Drawing Pad")

controls  =tk.Frame(root)
controls.grid(row=0,column=0,sticky="ew",padx=8,pady=8)

canvas=tk.Canvas(root,bg="white",width=760,height=480)
canvas.grid(row=1,column=0,sticky="nsew",padx=8,pady=8)

root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

























root.mainloop()

