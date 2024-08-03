# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

import math

reps = 0


def restart_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(20 * 60)
        my_label.config(text="Long Break")

    elif reps % 2 == 0:
        count_down(5 * 60)
        my_label.config(text="Short Break")

    else:
        count_down(25 * 60)
        my_label.config(text="Work Time")


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        start_timer()
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
            check_marks = Label(text=mark, fg=GREEN, bg=YELLOW)
            check_marks.grid(column=1, row=3)


from tkinter import *

window = Tk()
window.config(padx=100, pady=113, bg=YELLOW)
my_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
my_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)
my_button2 = Button(text="Stop", highlightthickness=0, command=restart_timer)
my_button2.grid(column=2, row=2)
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
