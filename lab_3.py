import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin

mashtab = 20

def f_coord(x):
    global mashtab
    return (x + 800//mashtab//2) * mashtab


def print_dots(x, y, color):
    global canvas
    x1 = x
    y1 = 800 - y
    canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=color)


def line(x0, y0, x1, y1):
    global canvas,mashtab
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
    for x in range(x1 + 1):
        if x % mashtab == 0:
            if y % mashtab < mashtab - y % mashtab:
                dots.append([x, y - y % mashtab])
            else:
                dots.append([x, y - y % mashtab + mashtab])
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
        print_dots(i[0] + xx0, i[1] + yy0, 'red')


def print_pixel(x1, y1):
    x = x1
    y = 800 - y1
    canvas.create_line(x, y, x, y + 1)


def draw_grid():
    global canvas,mashtab
    for i in range(800//mashtab):
        canvas.create_line(i * mashtab, 0, i * mashtab, 800)
        canvas.create_line(0, i * mashtab, 800, i * mashtab)


def draw_circle(x0, y0, radius):
    global canvas
    canvas.create_oval(x0 - radius, (800 - y0) - radius, x0 + radius, (800 - y0) + radius)
    x = 0
    y = radius
    delta = 1 - 2 * radius
    error = 0
    canvas.create_oval(400 - radius, 400 - radius, 400 + radius, 400 + radius)
    dots = []
    while y >= 0:
        if y == 0:
            dots.append([radius, y])
            dots.append([-radius, y])
            break
        # dots.append([x0 + x, y0 + y])
        # dots.append([x0 + x, y0 - y])
        # dots.append([x0 - x, y0 + y])
        # dots.append([x0 - x, y0 - y])
        dots.append([  x,   y])
        dots.append([  x,  - y])
        dots.append([ - x,  y])
        dots.append([ - x,  - y])
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += mashtab
            delta += 2 * x + mashtab
            continue
        if delta > 0 and error > 0:
            y -= mashtab
            delta += mashtab - 2 * y
            continue
        x += mashtab
        delta += 2 * (x - y)
        y -= mashtab
    for i in dots:
        print_dots(i[0]+400, i[1]+400, 'red')
    for i in dots:
        print_dots(i[0] + x0, i[1] + y0, 'blue')


xx1, yy1, xx2, yy2 = 14, 4, 11, -4
oxx, oyy, rr = -12, -10, 5
x1, y1, x2, y2 = f_coord(xx1), f_coord(yy1), f_coord(xx2), f_coord(yy2)
ox, oy, r = f_coord(oxx), f_coord(oyy), rr * mashtab
win = tk.Tk()
win.title("lab 3")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)
draw_grid()
print_dots(400, 400, 'black')
#line(x1, y1, x2, y2)
draw_circle(ox, oy, r)
win.mainloop()
