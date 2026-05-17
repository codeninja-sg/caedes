import tkinter as tk
import random   

root = tk.Tk()
root.title('Ball Drop')

W = 400
H = 500

canvas = tk.Canvas(root, width=W, height=H, bg="black")
canvas.pack()

pad_w = 90
pad_h = 12
pad_x= W //2
pad_y = H - 40

paddle = canvas.create_rectangle(pad_x - pad_w//2, pad_y - pad_h//2,
    pad_x + pad_w//2, pad_y + pad_h//2,
    fill='cyan', outline='')

SPEED = 20

def move_left(event):
    global pad_x
    pad_x -= SPEED

    if pad_x < pad_w //2:
        pad_x = pad_w//2 



root.mainloop()
