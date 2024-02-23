import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin

dots = []


def reset_dots():
    global dots
    dots.clear()
    for i in range(6):
        dots.append([cos(pi / 3 * i).real, sin(pi / 3 * i).real])


reset_dots()


def draw_canvas():
    def draw_line():
        print(1)

    print(1)


def change_coord():
    x = float(shift_x.get())
    y = float(shift_y.get())
    global dots
    for i in dots:
        i[0] += x
        i[1] += y
    draw_canvas()


def miracle_x():
    global dots
    for i in dots:
        i[0] = -i[0]
    draw_canvas()


def miracle_y():
    global dots
    for i in dots:
        i[1] = -i[1]
    draw_canvas()


def miracle_xy():
    global dots
    for i in dots:
        i[0], i[1] = i[1], i[0]
    draw_canvas()


def change_rotation():
    global dots
    x = float(rotation_x.get())
    y = float(rotation_y.get())
    alpha = float(rotation_a.get()) / 360 * 2 * pi
    for i in dots:
        if i[0] == x and i[1] == y:
            continue
        v_x = i[0] - x
        v_y = i[1] - y
        dist = sqrt(v_x ** 2 + v_y ** 2)
        v_x /= dist
        v_y /= dist
        cur_alpha = acos(v_x)
        if asin(v_y).real < 0:
            cur_alpha += pi
        cur_alpha += alpha
        v_x = cos(cur_alpha).real * dist
        v_y = sin(cur_alpha).real * dist
        i[0] = (x + v_x).real
        i[1] = (y + v_y).real
    draw_canvas()


def reset_and_print():
    reset_dots()
    draw_canvas()


win = tk.Tk()
win.title("lab 2 a")
win.geometry("1200x900")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)
draw_canvas()
# ------------------------------------------------------------
shift_x = tk.Entry(win, width=15)
shift_y = tk.Entry(win, width=15)
shift_x.insert(0, '0')
shift_y.insert(0, '0')
shift_x.place(x=850, y=50)
shift_y.place(x=950, y=50)
# ------------------------------------------------------------
label_shift_x = tk.Label(win, text="X")
label_shift_y = tk.Label(win, text="Y")
label_shift_x.place(x=885, y=30)
label_shift_y.place(x=985, y=30)
# ------------------------------------------------------------
button_shift = tk.Button(win, text='Переместить', command=change_coord)
button_shift.place(x=1100, y=50)
# ------------------------------------------------------------
label_miracle = tk.Label(win, text="Отразить ")
label_miracle.place(x=850, y=75)
# ------------------------------------------------------------
button_miracle_x = tk.Button(win, text='X', command=miracle_x)
button_miracle_x.place(x=850, y=100)
# ------------------------------------------------------------
button_miracle_y = tk.Button(win, text='Y', command=miracle_y)
button_miracle_y.place(x=900, y=100)
# ------------------------------------------------------------
button_miracle_xy = tk.Button(win, text='X=Y', command=miracle_xy)
button_miracle_xy.place(x=950, y=100)
# ------------------------------------------------------------
label_resize = tk.Label(win, text="Масштаб")
label_resize.place(x=850, y=125)
# ------------------------------------------------------------
resize_x = tk.Entry(win, width=15)
resize_y = tk.Entry(win, width=15)
resize_x.insert(0, '100')
resize_y.insert(0, '100')
resize_x.place(x=850, y=175)
resize_y.place(x=950, y=175)
# ------------------------------------------------------------
label_resize_x = tk.Label(win, text="X")
label_resize_y = tk.Label(win, text="Y")
label_resize_x.place(x=885, y=150)
label_resize_y.place(x=985, y=150)
# ------------------------------------------------------------
button_resize = tk.Button(win, text='Переместить', command=draw_canvas)
button_resize.place(x=1100, y=150)
# ------------------------------------------------------------
label_rotation = tk.Label(win, text="Поворот")
label_rotation.place(x=850, y=200)
# ------------------------------------------------------------
label_rotation_x = tk.Label(win, text="X")
label_rotation_y = tk.Label(win, text="Y")
label_rotation_a = tk.Label(win, text="a")
label_rotation_x.place(x=885, y=225)
label_rotation_y.place(x=985, y=225)
label_rotation_a.place(x=1085, y=225)
# ------------------------------------------------------------
rotation_x = tk.Entry(win, width=15)
rotation_y = tk.Entry(win, width=15)
rotation_a = tk.Entry(win, width=15)
rotation_x.insert(0, '0')
rotation_y.insert(0, '0')
rotation_a.insert(0, '0')
rotation_x.place(x=850, y=250)
rotation_y.place(x=950, y=250)
rotation_a.place(x=1050, y=250)
# ------------------------------------------------------------
button_rotation = tk.Button(win, text='Повернуть', command=change_rotation)
button_rotation.place(x=1100, y=275)
# ------------------------------------------------------------
button_rotation = tk.Button(win, text='Восстановить', command=reset_and_print)
button_rotation.place(x=1100, y=275)
win.mainloop()
