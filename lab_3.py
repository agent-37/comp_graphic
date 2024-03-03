import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin


def line(x0, y0, x1, y1):
    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    deltax = abs(x1 - x0)
    deltay = abs(y1 - y0)
    if deltax > deltay:
        print('i am here')
        error = 0
        deltaerr = (deltay + 1)
        y = y0
        diry = y1 - y0
        if diry > 0:
            diry = 1
        if diry < 0:
            diry = -1
        if x0 < x1:
            for x in range(x0, x1):
                print_pixel(x, y)
                error += deltaerr
                if error >= (deltax + 1):
                    y += diry
                    error -= (deltax + 1)
        else:
            for x in range(x0, x1, -1):
                print_pixel(x, y)
                error += deltaerr
                if error >= (deltax + 1):
                    y += diry
                    error -= (deltax + 1)
    else:
        error = 0
        deltaerr = (deltax + 1)
        x = x0
        dirx = x1 - x0
        if dirx > 0:
            dirx = 1
        if dirx < 0:
            dirx = -1
        if y0 < y1:
            for y in range(y0, y1):
                print_pixel(x, y)
                error += deltaerr
                if error >= (deltay + 1):
                    x += dirx
                    error -= (deltay + 1)
        else:
            for y in range(y0, y1, -1):
                print_pixel(x, y)
                error += deltaerr
                if error >= (deltay + 1):
                    x += dirx
                    error -= (deltay + 1)


def print_pixel(x, y):
    canvas.create_line(x, y, x, y + 1)


def draw_grid():
    global canvas
    for i in range(8):
        canvas.create_line(i * 100, 0, i * 100, 800)
        canvas.create_line(0, i * 100, 800, i * 100)


def draw_circle(x0, y0, radius):
    x = 0
    y = radius
    delta = 1 - 2 * radius
    error = 0
    while y >= 0:
        print_pixel(x0 + x, y0 + y)
        print_pixel(x0 + x, y0 - y)
        print_pixel(x0 - x, y0 + y)
        print_pixel(x0 - x, y0 - y)
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += 2 * x + 1
            continue
        if delta > 0 and error > 0:
            y -= 1
            delta += 1 - 2 * y
            continue
        x += 1
        delta += 2 * (x - y)
        y -= 1


x1, y1, x2, y2 = 400, 400, 600, 500
ox, oy, r = 200, 200, 100
win = tk.Tk()
win.title("lab 3")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)
draw_grid()
canvas.create_line(x1 + 100, y1 + 100, x2 + 100, y2 + 100)
line(x1, y1, x2, y2)
canvas.create_oval(ox - r + 200, oy - r , ox + r + 200, oy + r,outline='red')
draw_circle(ox, oy, r)
win.mainloop()
