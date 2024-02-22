import tkinter as tk

win = tk.Tk()
win.title("lab 2 a")
win.geometry("1200x900")
win.resizable(False, False)

canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

win.mainloop()
