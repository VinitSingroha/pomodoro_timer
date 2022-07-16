from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
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
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.config(bg="#100d14")
window.minsize(width=400, height=500)
title_label = Label(window, foreground="#5c2ae4", bg="#100d14", text="Timer", font=("Serif", 30, "bold"))
title_label.grid(row=0, column=3, pady=0)
start_button = Button(text="Start", bg="#5c2ae4", foreground="white", font=("Lucida Sans", 10, "bold"), border=10,
                      command=start_timer)
start_button.grid(row=2, column=2, padx=10)
reset_button = Button(text="Reset", bg="#5c2ae4", foreground="white", font=("Lucida Sans", 10, "bold"), border=10,
                      command=reset_timer)
reset_button.grid(row=2, column=4, padx=10)

canvas = Canvas(window, width=300, height=300, bg="#100d14", highlightthickness=0)
new_image = PhotoImage(file="2396.png")
canvas.create_image(150, 150, image=new_image)
timer_text = canvas.create_text(140, 150, text="00:00", fill="Pink", font=("Courier New", 20, "bold"))
canvas.grid(row=1, column=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
