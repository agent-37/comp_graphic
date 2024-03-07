import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin


def f_coord(x):
    return (x + 10) * 40


def print_dots(x, y,color):
    global canvas
    x1 = x
    y1 = 800 - y
    canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=color)


def line(x0, y0, x1, y1):
    global canvas
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    xx0, yy0, xx1, yy1 = x0, y0, x1, y1
    canvas.create_line(x0, 800 - (y0), x1, 800 - (y1))
    x1 -= x0
    y1 -= y0
    x0, y0 = 0, 0
    canvas.create_line(x0 + 400, 800 - (y0 + 400), x1 + 400, 800 - (y1 + 400), fill='green')
    flag_x, flag_x_y = 0, 0
    if y1 < 0:
        flag_x = 1
        y1 = abs(y1)
        canvas.create_line(x0 + 400, 800 - (y0 + 400), x1 + 400, 800 - (y1 + 400), fill='red')
    if y1 > x1:
        flag_x_y = 1
        y1, x1 = x1, y1
        canvas.create_line(x0 + 400, 800 - (y0 + 400), x1 + 400, 800 - (y1 + 400), fill='blue')
    error = 0
    dots = []
    y = 0
    deltaerr = (y1 + 1)
    for x in range(x1+1):
        if x % 40 == 0:
            if y % 40 < 40 - y % 40:
                dots.append([x, y - y % 40])
            else:
                dots.append([x, y - y % 40 + 40])
        error += deltaerr
        if error >= (x1 + 1):
            y += 1
            error -= (x1 + 1)
    # Точки если нужно показать на синем отрезке
    # for i in dots:
    #     print_dots(i[0] + 400, i[1] + 400, 'blue')
    if flag_x_y == 1:
        for i in dots:
            i[0], i[1] = i[1], i[0]
    if flag_x:
        for i in dots:
            i[1] = -i[1]
    for i in dots:
        print_dots(i[0] + xx0, i[1] + yy0,'red')



def print_pixel(x1, y1):
    x = x1
    y = 800 - y1
    canvas.create_line(x, y, x, y + 1)


def draw_grid():
    global canvas
    for i in range(20):
        canvas.create_line(i * 40, 0, i * 40, 800)
        canvas.create_line(0, i * 40, 800, i * 40)


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


xx1, yy1, xx2, yy2 = 4, 4, 1, -4
oxx, oyy, rr = 2, 2, 1
x1, y1, x2, y2 = f_coord(xx1), f_coord(yy1), f_coord(xx2), f_coord(yy2)
win = tk.Tk()
win.title("lab 3")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)
draw_grid()
# canvas.create_line(x1 + 100, y1 + 100, x2 + 100, y2 + 100)
line(x1, y1, x2, y2)
# canvas.create_oval(ox - r + 200, oy - r, ox + r + 200, oy + r, outline='red')
# draw_circle(ox, oy, r)
win.mainloop()
