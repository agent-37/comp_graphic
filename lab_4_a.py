import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin
from math import ceil

mashtab = 20


def print_dots(x, y, color):
    global canvas
    x1 = x
    y1 = 800 - y
    canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=color)


def f_coord(x):
    global mashtab
    return (x + 800 // mashtab // 2) * mashtab


def draw_grid():
    global canvas, mashtab
    for i in range(800 // mashtab):
        canvas.create_line(i * mashtab, 0, i * mashtab, 800)
        canvas.create_line(0, i * mashtab, 800, i * mashtab)


n = int(input('Введите количество точек\n'))
dots = []


def input_dots():
    global n, dots
    for i in range(n):
        x, y = map(int, input().split())
        dots.append([x, y])


def check_coord():
    global n, dots

    def vect_num(ax, ay, bx, by):
        return ax * by - ay * bx

    AB, BC = [dots[1][0] - dots[0][0], dots[1][1] - dots[0][1]], [dots[2][0] - dots[1][0], dots[2][1] - dots[1][1]]
    if vect_num(AB[0], AB[1], BC[0], BC[1]) < 0:
        # dots = reversed(dots)
        buf = []
        for i in range(n):
            buf.append(dots[n - i - 1])
        dots = buf


def find_mask(ax, ay):
    global l, r, u, d
    if ax < l and ay < d:
        return 9
    if ax <= l and u >= ay >= d:
        return 1
    if ax < l and ay < u:
        return 3
    if l <= ax <= r and ay <= d:
        return 8
    if l < ax < r and d < ay < u:
        return 0
    if l <= ax <= r and u <= ay:
        return 2
    if r < ax and ay < d:
        return 12
    if r <= ax and d <= ay <= u:
        return 4
    if r < ax and u < ay:
        return 6


input_dots()
check_coord()
l, r, u, d = 1e10, 1e-10, 1e-10, 1e10
for i in range(n):
    l = min(l, dots[i][0])
    r = max(r, dots[i][0])
    u = max(u, dots[i][1])
    d = min(d, dots[i][1])

ax, ay, bx, by = map(int, input('Введите концы отрезка\n').split())
A, B = [ax, ay], [bx, by]

flag = 1
if find_mask(ax, ay) & find_mask(bx, by) != 0:
    flag = 0
if (find_mask(ax, ay) == 0 and find_mask(bx, by) != 0) or (find_mask(bx, by) == 0 and find_mask(ax, ay) != 0):
    flag = -1

win = tk.Tk()
win.title("lab 4")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

draw_grid()

canvas.create_rectangle(f_coord(l), 800 - f_coord(d), f_coord(r), 800 - f_coord(u), outline='red')
canvas.create_line(f_coord(ax), 800 - f_coord(ay), f_coord(bx), 800 - f_coord(by), fill='blue')
t = set()


def check_pere(P1, P2, A, B):
    global t
    P2P1 = [P1[0] - P2[0], P1[1] - P2[1]]
    N = [-P2P1[1], P2P1[0]]
    if (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1])) == 0:
        return
    tt = (N[0] * P1[0] - A[0] * N[0] + N[1] * P1[1] - N[1] * A[1]) / (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1]))
    if tt > 1 or tt < 0:
        return
    if min(P1[0], P2[0]) <= A[0] + tt * (B[0] - A[0]) <= max(P1[0], P2[0]) and min(P1[1], P2[1]) <= A[1] + tt * (
            B[1] - A[1]) <= max(P1[1], P2[1]):
        t.add(tt)


if abs(flag):
    if flag == 1:
        for i in range(n - 1):
            check_pere(dots[i], dots[i + 1], A, B)
        check_pere(dots[n - 1], dots[0], A, B)
        pr_dots = []
        for i in t:
            pr_dots.append([ceil(f_coord((1 - i) * A[0] + i * B[0])), ceil(f_coord((1 - i) * A[1] + i * B[1]))])
        for i in pr_dots:
            print_dots(i[0], i[1], 'green')
        # print(pr_dots)
        if len(pr_dots) >= 2:
            canvas.create_line(pr_dots[0][0], 800 - pr_dots[0][1], pr_dots[1][0], 800 - pr_dots[1][1], fill='orange')
    else:
        for i in range(n - 1):
            check_pere(dots[i], dots[i + 1], A, B)
        check_pere(dots[n - 1], dots[0], A, B)
        print(t)
win.mainloop()
