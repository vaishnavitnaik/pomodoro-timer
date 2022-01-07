from os import terminal_size
from tkinter import *
import math
from typing import ChainMap
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(my_timer)
    check_marks.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps +=1
    work_sec=  WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1,3,5,7]:
        title_label.config(text="Work",fg=GREEN)
        countdown(work_sec)
    elif reps == 8:
        title_label.config(text="Break",fg=RED)
        countdown(long_break_sec)
    elif reps in [2,4,6]:
        title_label.config(text="Break",fg=PINK)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global my_timer
    count_min= math.floor(count / 60)
    count_sec= math.floor(count%60)

    if count_sec<10:
        count_sec=f"0{count_sec}"  #python dynamic typing

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if(count>0):
        my_timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        tick = ""
        for _ in range (math.floor(reps/2)):
            tick += "✓"
            check_marks.config(text=tick)


              


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)




title_label= Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(row=0,column=1)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=0)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)
check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=4)


canvas = Canvas(width=220,height=224,bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="tomato.png") 
canvas.create_image(110,112,image=tomato)
timer_text= canvas.create_text(110,120,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=1,row=1)





window.mainloop()