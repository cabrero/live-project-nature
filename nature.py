#!/usr/bin/env python3

import random
import time
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


def drop(canvas, i, j):
    x = i * COL_STEP
    y = j * ROW_STEP
    r = INIT_SIZE // 2
    return (canvas.create_oval(x-r, y-r, x+r, y+r , fill= "black"), x, y, INIT_SIZE)

def update(canvas, drops):
    for col in drops:
        for drop in col:
            drop_id, x, y, sz = drop
            r = sz // 2
            canvas.coords(drop_id, x-r, y-r, x+r, y+r)
    canvas.update()

def reset_drop(drop):
    drop_id, x, y, sz = drop
    return (drop_id, x, y, INIT_SIZE)

def grow(drop):
    drop_id, x, y, sz = drop
    if random.uniform(0, 10) < RAIN_RATE:
        sz = sz + DROP_INCREASE
    if sz > RESET_SIZE:
        sz = INIT_SIZE
        falling = True
    else:
        falling = False
    return (drop_id, x, y, sz), falling

def grow_col(col):
    new_col = []
    falling_drops = False
    for drop in col:
        if falling_drops:
            drop = reset_drop(drop)
        else:
            drop, falling_drops = grow(drop)
        new_col.append(drop)
    return new_col
        
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

    drops = [ [ drop(canvas,i , j) for j in range(0, NROWS)] for i in range(0, NCOLS) ]

    
    while True:
        update(canvas, drops)
        drops = [ grow_col(col) for col in drops ]
        time.sleep(0.5)
        
    #window.mainloop()

    
if __name__ == '__main__':
    main()
