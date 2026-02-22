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

current_colour = "black"
pen_size = 5
last_x,last_y= None, None

def start_draw(event):
    global last_x,last_y
    last_x,last_y = event.x,event.y

def draw(event):
    global last_x,last_y
    if last_x is not None and last_y is not None:
       canvas.create_line(last_x,last_y,event.x,event.y, fill=current_colour,width=pen_size,capstyle=tk.ROUND)

    last_x,last_y = event.x,event.y

def end_draw(event):
    global last_x, last_y
    last_x, last_y = None, None
    
                       
canvas.bind("<Button-1>",start_draw)
canvas.bind("<B1-Motion>",draw)
canvas.bind("<ButtonRelease-1>", end_draw)





















root.mainloop()
