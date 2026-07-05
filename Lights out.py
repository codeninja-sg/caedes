grid = [
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]
]

ROWS = 5
COLS = 5
root = tk.TK()
root.title('Lights Out')

ROWS = 5
COLS = 5

grid= [[0]* COLS for _ in range(ROWS)]


buttons = []

for r in range(ROWS):
    for c in range(COLS):