import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin
import time
from math import ceil


def print_dots(x, y, color):
    global canvas
    x1 = x
    y1 = 800 - y
    canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill=color)


def print_pixel(x, y, color):
    global canvas
    x1 = x
    # y1 = 800 - y
    y1 = y
    canvas.create_line(x1, y1, x1, y1 + 1, fill=color)


def line(x0, y0, x1, y1):
    global canvas, matrix
    mashtab = 1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    xx0, yy0, xx1, yy1 = x0, y0, x1, y1
    # canvas.create_line(x0, y0, x1, y1)
    x1 -= x0
    y1 -= y0
    flag_x, flag_x_y = 0, 0
    if y1 < 0:
        flag_x = 1
        y1 = abs(y1)
    if y1 > x1:
        flag_x_y = 1
        y1, x1 = x1, y1
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
    if flag_x_y == 1:
        for i in dots:
            i[0], i[1] = i[1], i[0]
    if flag_x:
        for i in dots:
            i[1] = -i[1]
    for i in dots:
        print_pixel(i[0] + xx0, i[1] + yy0, 'black')
        matrix[i[0] + xx0][i[1] + yy0] = 1


win = tk.Tk()
win.title("lab 5")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

matrix = [[0 for j in range(800)] for i in range(800)]
f_file = open("5.txt", "r")
n = int(f_file.readline())
dots = []
for i in range(n):
    dots.append(list(map(int, f_file.readline().split())))

for i in range(n - 1):
    line(dots[i][0], dots[i][1], dots[i + 1][0], dots[i + 1][1])
line(dots[0][0], dots[0][1], dots[n - 1][0], dots[n - 1][1])
x, y = map(int, input('Введите точку\n').split())
q = [[x, y]]
while len(q) != 0:
    cur = q.pop(0)
    # print(cur, matrix[cur[0]][cur[1]])
    if matrix[cur[0]][cur[1]] == 1:
        continue

    matrix[cur[0]][cur[1]] = 1
    print_pixel(cur[0], cur[1], 'black')
    win.update()
    # time.sleep(0.01)
    q.append([cur[0] + 1, cur[1]])
    q.append([cur[0] - 1, cur[1]])
    q.append([cur[0], cur[1] + 1])
    q.append([cur[0], cur[1] - 1])
win.mainloop()
