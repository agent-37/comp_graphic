import tkinter as tk

coord_pl = [400, 800]
coord_bot = [400, 0]
coord_box = [400, 400]
siz_box = 10
siz_height = 20
siz_weight = 50
step = 10


def draw_canvas():
    global canvas

    def clear_board():
        canvas.create_polygon(0, 0, 0, 800, 800, 800, 800, 0, fill='white')

    def make_line(a, b):
        canvas.create_line(a[0], a[1], b[0], b[1])

    def print_pl():
        canvas.create_rectangle(coord_pl[0] - siz_weight, coord_pl[1] - siz_height, coord_pl[0] + siz_weight,
                                coord_pl[1], fill='black')

    def print_bot():
        canvas.create_rectangle(coord_bot[0] - siz_weight, coord_bot[1] + siz_height, coord_bot[0] + siz_weight,
                                coord_bot[1], fill='black')

    def print_box():
        canvas.create_rectangle(coord_box[0] - siz_box, coord_box[1] - siz_box, coord_box[0] + siz_box,
                                coord_box[1] + siz_box, fill='black')

    clear_board()
    print_pl()
    print_bot()
    print_box()


def press_key(event):
    global coord_pl
    if event.char == 'd':
        if (coord_pl[0] + siz_weight + step <= coord_box[0] - siz_box or coord_pl[1] - siz_height > coord_box[
            1] + siz_box) \
                and coord_pl[0] + siz_weight + step <= 800:
            coord_pl[0] += step
    if event.char == 'a':
        if (coord_pl[0] - siz_weight - step >= coord_box[0] + siz_box or coord_pl[1] - siz_height > coord_box[
            1] + siz_box) \
                and coord_pl[0] - siz_weight - step >= 0:
            coord_pl[0] -= step
    draw_canvas()


def tick():
    win.after(200, tick)
    if (coord_bot[0] + siz_weight + step <= coord_box[0] - siz_box or coord_bot[1] + siz_height < coord_box[
        1] + siz_box) \
            and coord_bot[0] + siz_weight + step <= 800:
        if coord_bot[0] < coord_box[0]:
            coord_bot[0] += step
    if (coord_bot[0] - siz_weight - step >= coord_box[0] + siz_box or coord_bot[1] + siz_height < coord_box[
        1] + siz_box) \
            and coord_bot[0] - siz_weight - step >= 0:
        if coord_bot[0] > coord_box[0]:
            coord_bot[0] -= step

    draw_canvas()


win = tk.Tk()
win.title("lab 2 a")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)
# -------------------------------------------------------------
win.bind('<Key>', press_key)
tick()
win.mainloop()
