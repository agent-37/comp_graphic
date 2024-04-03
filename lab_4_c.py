import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin
import time
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
    global dots
    b_dots = []
    for i in dots:
        b_dots.append([int(f_coord(i[0])), int(f_coord(i[1]))])
    l, r, u, d = int(1e10), int(1e-10), int(1e-10), int(1e10)

    for i in range(n):
        l = min(l, b_dots[i][0])
        r = max(r, b_dots[i][0])
        u = max(u, b_dots[i][1])
        d = min(d, b_dots[i][1])
    if ax < l and ay < d:
        return 9
    if ax < l and d <= ay <= u:
        return 1
    if ax < l and u < ay:
        return 3
    if l <= ax <= r and ay < d:
        return 8
    if l <= ax <= r and d <= ay <= u:
        return 0
    if l <= ax <= r and u < ay:
        return 2
    if r < ax and ay < d:
        return 12
    if r < ax and d <= ay <= u:
        return 4
    if r < ax and u < ay:
        return 6


def rec_bin_dot(A, B):
    if abs(A[0] - B[0]) <= 1 and abs(A[1] - B[1]) <= 1:
        return
    mid = [(A[0] + B[0]) >> 1, (A[1] + B[1]) >> 1]

    m_A, m_B, m_mid = find_mask(A[0], A[1]), find_mask(B[0], B[1]), find_mask(mid[0], mid[1])
    print(A, m_A, B, m_B)
    if m_A == 0 and m_mid == 0:
        canvas.create_line(A[0], 800 - A[1], mid[0], 800 - mid[1], fill='orange')
    if m_B == 0 and m_mid == 0:
        canvas.create_line(B[0], 800 - B[1], mid[0], 800 - mid[1], fill='orange')
    print_dots(mid[0], mid[1], 'green')
    win.update()
    time.sleep(0.5)
    if m_A & m_mid == 0 and (m_A != 0 or m_mid != 0):
        rec_bin_dot(A, mid)
    if m_B & m_mid == 0 and (m_B != 0 or m_mid != 0):
        rec_bin_dot(mid, B)


n = int(input('Введите количество точек\n'))
dots = []

input_dots()
print('Введите концы отрезка')
A, B = [int(input()) for i in range(2)], [int(input()) for j in range(2)]
win = tk.Tk()
win.title("lab 4")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

draw_grid()

canvas.create_rectangle(f_coord(dots[0][0]), 800 - f_coord(dots[0][1]), f_coord(dots[2][0]), 800 - f_coord(dots[2][1]),
                        outline='red')
canvas.create_line(f_coord(A[0]), 800 - f_coord(A[1]), f_coord(B[0]), 800 - f_coord(B[1]), fill='blue')
print_dots(f_coord(A[0]), f_coord(A[1]), 'green')
print_dots(f_coord(B[0]), f_coord(B[1]), 'green')
f_A, f_B = [f_coord(A[0]), f_coord(A[1])], [f_coord(B[0]), f_coord(B[1])]
rec_bin_dot(f_A, f_B)
win.mainloop()
