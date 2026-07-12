import tkinter as tk

grid = [
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]
]

ROWS = 5
COLS = 5
root = tk.Tk()
root.title('Lights Out')

ROWS = 5
COLS = 5

grid= [[0]* COLS for _ in range(ROWS)]


buttons = []

for r in range(ROWS):
    for c in range(COLS):
        btn = tk.Button(root, width=6, height=3, bg='grey20')
        btn.grid(row=r, column=c, padx=2, pady=2)
        buttons.append(btn)

root.mainloop()        
