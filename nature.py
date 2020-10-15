#!/usr/bin/env python3

import tkinter as tk


WIDTH   = 1000
HEIGHT  = 1000
PADDING = 10

NROWS = 20
NCOLS = 20

COL_STEP = WIDTH // NCOLS
ROW_STEP = HEIGHT // NROWS

RAIN_RATE = 0.1
INIT_SIZE = 2
DROP_INCREASE = 5
RESET_SIZE = 50

def update(canvas, drops):
    for i, col in enumerate(drops):
        for j, sz in enumerate(col):
            x = i * COL_STEP
            y = j * ROW_STEP
            r = sz // 2
            canvas.create_oval(x - r, y - r, x + r, y + r)
            
def main():
    window = tk.Tk()
    window.title("Live Project: Simulating Nature")
    window.geometry(f"{WIDTH+PADDING}x{HEIGHT+PADDING}")
    window.configure(bg= 'white')
    
    canvas = tk.Canvas(master= window, width= WIDTH, height= HEIGHT)
    canvas.pack(anchor= tk.CENTER, expand= False)

    for col in range(0, WIDTH, COL_STEP):
        for row in range(0, HEIGHT, ROW_STEP):
            canvas.create_line(0, row, WIDTH, row)
            canvas.create_line(col, 0, col, HEIGHT)

    drops = [ [ INIT_SIZE for _ in range(0, NROWS)] for _ in range(0, NCOLS) ]

    update(canvas, drops)
    
    window.mainloop()

    
if __name__ == '__main__':
    main()
