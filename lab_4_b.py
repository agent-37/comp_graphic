import struct
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


def find_mask(ax, ay):
    global l, r, u, d

    if l <= ax <= r and d <= ay <= u:
        return 0
    if ax < l and ay < d:
        return 9
    if ax <= l and u >= ay >= d:
        return 1
    if ax < l and ay < u:
        return 3
    if l <= ax <= r and ay <= d:
        return 8
    if l <= ax <= r and u <= ay:
        return 2
    if r < ax and ay < d:
        return 12
    if r <= ax and d <= ay <= u:
        return 4
    if r < ax and u < ay:
        return 6


input_dots()
l, r, u, d = 1e10, 1e-10, 1e-10, 1e10
for i in range(n):
    l = min(l, f_coord(dots[i][0]))
    r = max(r, f_coord(dots[i][0]))
    u = max(u, f_coord(dots[i][1]))
    d = min(d, f_coord(dots[i][1]))

ax, ay, bx, by = map(int, input('Введите концы отрезка\n').split())
ax, ay, bx, by = f_coord(ax), f_coord(ay), f_coord(bx), f_coord(by)
# A, B = [ax, ay], [bx, by]


win = tk.Tk()
win.title("lab 4")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

draw_grid()
canvas.create_rectangle(l, 800 - d, r, 800 - u, outline='red')

if find_mask(ax, ay) == 0 and find_mask(bx, by) == 0:
    canvas.create_line(ax, 800 - ay, bx, 800 - by, fill='orange')
    print_dots(ax, ay, 'green')
    print_dots(bx, by, 'green')
else:
    class line:
        A, B, C = 0, 0, 0

        def set(self, Ax, Ay, Bx, By):
            if Ax - Bx != 0:
                self.A = (By - Ay) / (Ax - Bx)
                self.B = 1
                self.C = (-Bx) * self.A + (-By) * self.B
            else:
                self.B = 0
                self.A = 1
                self.C = (-Bx) * self.A + (-By) * self.B


    def find_point(A, B):
        Tx, Ty = 0, 0
        if A.A == B.A and A.B == B.B:
            return
        if (A.A == 0):
            Ty = -A.C / A.B
            Tx = -Ty * (B.B / B.A) - B.C / B.A
            return [Tx, Ty]
        else:
            if (B.A == 0):
                Ty = -B.C / B.B
                Tx = -Ty * (A.B / A.A) - A.C / A.A
                return [Tx, Ty]
            else:
                Ty = (A.C / A.A - B.C / B.A) / (B.B / B.A - A.B / A.A)
                Tx = -Ty * (A.B / A.A) - A.C / A.A
                return [Tx, Ty]


    def make_line(Ax, Ay, Bx, By):
        l = line()
        l.set(Ax, Ay, Bx, By)
        return l


    lines = [make_line(l, u, l, d), make_line(l, u, r, u), make_line(r, u, r, d), make_line(l, d, r, d)]

    dots = []
    ll = make_line(ax, ay, bx, by)
    for i in lines:
        buf = find_point(i, ll)
        if buf is not None and min(ax, bx) <= buf[0] <= max(ax, bx) and min(ay, by) <= buf[1] <= max(ay, by):
            dots.append(buf)
    dots.append([ax, ay])
    dots.append([bx, by])
    canvas.create_line(ax, 800 - ay, bx, 800 - by)
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            aax, aay, bbx, bby = ceil(dots[i][0]), ceil(dots[i][1]), ceil(dots[j][0]), ceil(dots[j][1])

            if find_mask(aax, aay) == 0 and find_mask(bbx, bby) == 0:
                canvas.create_line(aax, 800 - aay, bbx, 800 - bby, fill='orange')
        print_dots(ceil(dots[i][0]), ceil(dots[i][1]), 'green')
win.mainloop()

# 4
# 0 0
# 5 0
# 5 4
# 0 4
# Введите концы отрезка
# 1 1 2 2
