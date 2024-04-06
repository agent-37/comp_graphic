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


def check_pere_for_more(P1, P2, A, B):
    P2P1 = [P1[0] - P2[0], P1[1] - P2[1]]
    N = [-P2P1[1], P2P1[0]]
    if (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1])) == 0:
        return
    tt = (N[0] * P1[0] - A[0] * N[0] + N[1] * P1[1] - N[1] * A[1]) / (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1]))
    # if tt > 1 or tt < 0:
    #     return
    return tt


def check_in(X):
    global dots
    flag = 1
    n = len(dots)

    def sign(AB, BC):
        if AB[0] * BC[1] - AB[1] * BC[0] > 0:
            return 0
        return 1

    for i in range(n - 1):
        flag = flag & sign([X[0] - dots[i][0], X[1] - dots[i][1]],
                           [dots[i + 1][0] - dots[i][0], dots[i + 1][1] - dots[i][1]])
    flag = flag & sign([X[0] - dots[n - 1][0], X[1] - dots[n - 1][1]],
                       [dots[0][0] - dots[n - 1][0], dots[0][1] - dots[n - 1][1]])
    return flag


n = int(input('Введите количество точек\n'))
dots = []
input_dots()
check_coord()

ax, ay, bx, by = map(int, input('Введите концы отрезка\n').split())
A, B = [ax, ay], [bx, by]

win = tk.Tk()
win.title("lab 4")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

draw_grid()
for i in range(n - 1):
    canvas.create_line(f_coord(dots[i][0]), 800 - f_coord(dots[i][1]), f_coord(dots[i + 1][0]),
                       800 - f_coord(dots[i + 1][1]), fill='red')
canvas.create_line(f_coord(dots[0][0]), 800 - f_coord(dots[0][1]), f_coord(dots[n - 1][0]),
                   800 - f_coord(dots[n - 1][1]), fill='red')
canvas.create_line(f_coord(ax), 800 - f_coord(ay), f_coord(bx), 800 - f_coord(by), fill='blue')

t = set()
for i in range(n - 1):
    check_pere(dots[i], dots[i + 1], A, B)
check_pere(dots[n - 1], dots[0], A, B)

t_all = []
for i in range(n - 1):
    buf = check_pere_for_more(dots[i], dots[i + 1], A, B)
    if buf is not None:
        t_all.append(check_pere_for_more(dots[i], dots[i + 1], A, B))
buf = check_pere_for_more(dots[n - 1], dots[0], A, B)
if buf is not None:
    t_all.append(check_pere_for_more(dots[n - 1], dots[0], A, B))
mi, ma = 2, -1
print(len(t))
if len(t) > 0:
    pr_dots = []
    for i in t:
        pr_dots.append([ceil(f_coord((1 - i) * A[0] + i * B[0])), ceil(f_coord((1 - i) * A[1] + i * B[1]))])
        mi = min(mi, i)
        ma = max(ma, i)
    if len(pr_dots) == 2:
        canvas.create_line(pr_dots[0][0], 800 - pr_dots[0][1], pr_dots[1][0], 800 - pr_dots[1][1], fill='orange')
    else:
        buf = []
        if check_in(A):
            buf = A
        else:
            buf = B
        canvas.create_line(pr_dots[0][0], 800 - pr_dots[0][1], f_coord(buf[0]), 800 - f_coord(buf[1]), fill='orange')
    for i in pr_dots:
        print_dots(i[0], i[1], 'green')
else:
    if check_in(A) and check_in(B):
        canvas.create_line(f_coord(A[0]), 800 - f_coord(A[1]), f_coord(B[0]), 800 - f_coord(B[1]), fill='orange')
    else:
        canvas.create_line(f_coord(A[0]), 800 - f_coord(A[1]), f_coord(B[0]), 800 - f_coord(B[1]),fill='blue')
before, after = [], []
print(t_all)
for i in t_all:
    if mi is None:
        before.append([ceil(f_coord((1 - i) * A[0] + i * B[0])), ceil(f_coord((1 - i) * A[1] + i * B[1]))])
    else:
        if i < mi:
            before.append([ceil(f_coord((1 - i) * A[0] + i * B[0])), ceil(f_coord((1 - i) * A[1] + i * B[1]))])
        else:
            if i > ma:
                after.append([ceil(f_coord((1 - i) * A[0] + i * B[0])), ceil(f_coord((1 - i) * A[1] + i * B[1]))])

print_dots(f_coord(A[0]), f_coord(A[1]), 'green')
print_dots(f_coord(B[0]), f_coord(B[1]), 'green')
for i in before:
    print_dots(i[0], i[1], 'red')
for i in after:
    print_dots(i[0], i[1], 'purple')

win.mainloop()
#
# 7
# 0 0
# 5 0
# 7 2
# 7 5
# 6 7
# 3 7
# 0 6


#
# 8
# 2 0
# 4 0
# 6 2
# 6 4
# 4 6
# 2 6
# 0 4
# 0 2
