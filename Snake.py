import tkinter as tk
import random

root=tk.Tk()
root.title('Snake-1')

SIZE = 20
W = 400
H = 400

canvas = tk.Canvas(root,width=W,height=H,bg='white')
canvas.pack()

snake=[(10,10)]

dx = 1
dy = 0
 
food = (random.randint(0, W//SIZE - 1),
       random.randint(0, H//SIZE - 1))

def draw():
    canvas.delete ('all')

    fx,fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE, fx*SIZE+SIZE,fy*SIZE+SIZE,fill='red') 
    
    for (x,y) in snake:
        canvas.create_rectangle(x*SIZE,y*SIZE,x*SIZE+SIZE,y*SIZE+SIZE,fill='green')

def game_loop():
    global snake,food
    max_x=W//SIZE
    max_y=H//SIZE

    head_x,head_y=snake[0]
    new_head = (head_x+dx,head_y+dy)
    


    if new_head[0]< 0 or new_head[0] >= max_x or new_head[1] < 0 or new_head[1] >= max_y or new_head in snake:
        print("Game Over")
        root.quit()
    

    if new_head in snake:
        print("Game Over")
        root.quit()

    snake.insert(0,new_head)

    if new_head==food:
        food = (random.randint(0,W//SIZE - 1),
                random.randint(0,H//SIZE - 1))
    else:
        snake.pop()

    draw()
    root.after(150,game_loop) 

def up(event):
    global dx, dy
    dx, dy = 0, -1

def down(event):
    global dx, dy
    dx, dy = 0, 1

def left(event):
    global dx, dy
    dx, dy=-1, 0

def right(event):
    global dx, dy
    dx, dy = 1, 0

def restart():
     global snake, dx, dy, food, game_over
     # snake = [(10, 10)]
     dx, dy = 1, 0

     food = (random.randint(0, max_x - 1),
         random.randint(0, max_y - 1))
    
     game_over = False
     #status_label.config(text="")
     draw()
     root.after(150, game_loop)

root.bind("<Up>",up)
root.bind("<Down>",down)
root.bind("<Left>",left)
root.bind("<Right>",right)

restart_btn = tk.Button(root, text="Restart", command=restart)                        
restart_btn.pack(pady=5)

game_loop()
draw()
root.mainloop()

