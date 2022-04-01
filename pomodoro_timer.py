from tkinter import *
import math


#setting constants
pink="#e2979c"
red="#e7305b"
green="#9bdeac"
yellow="#f7efdd"
font_name='Consolas'
work_min=25
short_break_min=5
long_break_min=20
reps=0
timer= None
title_lable= Label(text="Timer", fg=green, bg=yellow, font=(font_name, 50))

#timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_lable.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

#timer mechanism
def start_timer():
    global reps
    reps +=1
    work_sec = work_min * 60
    short_break_sec=short_break_min*60
    long_break_sec=long_break_min*60

    if reps % 8 ==0:
        count_down(long_break_sec)
        title_lable.config(text="Break",fg=red)
    elif reps %2 ==0:
        count_down(short_break_sec)
        title_lable.config(text="Break",fg=pink)
    else:
        count_down(work_sec)
        title_lable.config(text="Work",fg=green)
#Countdown mechanism

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

#UI Set-up
window = Tk()
window.title("Pomodoro")
window.config(padx=300, pady=150, bg=yellow)

title_lable= Label(text="Timer", fg=green, bg=yellow, font=(font_name, 50))
title_lable.grid(column=0, row=0)

canvas = Canvas(width=800, height=680, bg=yellow, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(350, 400, image=tomato_img)
timer_text=canvas.create_text(320, 430, text="00:00", fill = "white", font=(font_name, 50))
canvas.grid(column=0, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=start_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=green, bg =yellow)
check_marks.grid(column=1, row=3)

window.mainloop()


