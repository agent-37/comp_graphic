import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin
import time
from math import ceil


def print_dots(x, y, color):
    global canvas
    x1 = x
    # y1 = 800 - y
    y1 = y
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


def cross_AB_AC(A, B, C):
    AB = [B[0] - A[0], B[1] - A[1]]
    AC = [C[0] - A[0], C[1] - A[1]]
    return AB[0] * AC[1] - AB[1] * AC[0]


def build_Endru(l, sign):
    global canvas
    st = [l[0]]
    for i in range(1, len(l)):
        print(l[i], '!!!')
        while len(st) >= 2 and cross_AB_AC(st[len(st) - 1], st[len(st) - 2], l[i]) * sign < 0:
            canvas.create_line(st[len(st) - 1][0], st[len(st) - 1][1], l[i][0], l[i][1], fill='red')
            canvas.create_line(st[len(st) - 1][0], st[len(st) - 1][1], st[len(st) - 2][0], st[len(st) - 2][1],
                               fill='red')
            win.update()
            time.sleep(0.5)
            st.pop()

        canvas.create_line(st[len(st) - 1][0], st[len(st) - 1][1], l[i][0], l[i][1], fill='black')
        st.append(l[i])
        win.update()
        time.sleep(0.5)


win = tk.Tk()
win.title("lab 6")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

f_file = open("6.txt", "r")
n = int(f_file.readline())
dots = []
for i in range(n):
    dots.append(list(map(int, f_file.readline().split())))

left, right = dots[0], dots[0]
for i in dots:
    if i[0] < left[0] or (i[0] == left[0] and i[1] < left[1]):
        left = i
    if i[0] > right[0] or (i[0] == right[0] and i[1] > right[1]):
        right = i
up, down = [], []
for i in dots:
    if cross_AB_AC(left, right, i) >= 0:
        up.append(i)
    else:
        down.append(i)
down.append(left)
down.append(right)
up.sort()
down.sort()

for i in dots:
    print_dots(i[0], i[1], 'black')
build_Endru(up, 1)
build_Endru(down, -1)
win.mainloop()
