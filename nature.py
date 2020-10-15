#!/usr/bin/env python3

import tkinter as tk


WIDTH   = 1000
HEIGHT  = 1000
PADDING = 10

NROWS = 20
NCOLS = 20

def main():
    window = tk.Tk()
    window.title("Live Project: Simulating Nature")
    window.geometry(f"{WIDTH+PADDING}x{HEIGHT+PADDING}")
    window.configure(bg= 'white')
    
    canvas = tk.Canvas(master= window, width= WIDTH, height= HEIGHT)
    canvas.pack(anchor= tk.CENTER, expand= False)

    for col in range(0, WIDTH, WIDTH // NCOLS):
        for row in range(0, HEIGHT, HEIGHT // NROWS):
            canvas.create_line(0, row, WIDTH, row)
            canvas.create_line(col, 0, col, HEIGHT)
    window.mainloop()

    
if __name__ == '__main__':
    main()
