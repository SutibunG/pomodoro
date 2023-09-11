from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CHECK = "✔"
BLUE = "#053B50"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
PAUSED = False
paused_tracker = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global PAUSED
    global paused_tracker

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")

    reps = 0
    paused_tracker = 0
    pause_button.config(text="  Pause ")
    PAUSED = False

    start_button["state"] = NORMAL


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global paused_tracker
    global PAUSED

    start_button["state"] = DISABLED

    reps += 1  

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break!", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global PAUSED
    global timer
    global paused_time


    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if PAUSED == False:
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        elif count == 0:
            window.attributes('-topmost', True)
            window.attributes('-topmost', False)
            start_timer()
            marks = ""
            work_sessions = reps // 2
            for _ in range(work_sessions):
                marks += CHECK
            check_label.config(text=marks, fg=GREEN)
    else:
        timer = window.after(0, count_down, count - 0)


# ---------------------------- PAUSE MECHANISM ------------------------------- # 
def pause_timer():
    global paused_tracker
    global PAUSED
    global timer

    paused_tracker += 1

    if paused_tracker % 2 != 0:
        PAUSED = True
        pause_button.config(text="Resume")
    else:
        PAUSED = False
        pause_button.config(text="  Pause ")
        

    print(PAUSED)
    print(paused_tracker)


# ---------------------------- PAUSE MECHANISM ------------------------------- #
def settings_menu():
    ...


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Sessions")
window.minsize(width=450, height=300)
window.maxsize(width=450, height=300)
window.config(padx=20,pady=20, bg=BLUE)

#Label
timer_label = Label(text="Timer", bg=BLUE,fg=GREEN, font=("Arial", 25, "bold"))
timer_label.place(x=150, y=20)


#Canvas
canvas = Canvas(width=450, height=250, bg=BLUE, highlightthickness=0)
timer_text = canvas.create_text(200, 60, text="00:00", fill="white", font=(FONT_NAME, 90, "bold"))
canvas.place(x=0, y=60)


#Start Button
start_button = Button(text="  Start  ", font=("Arial", 15, "bold"), command=start_timer)
start_button.place(x=50, y=200)

#Pause Button
pause_button = Button(text="  Pause ", font=("Arial", 15, "bold"), command=pause_timer)
pause_button.place(x=155, y=200)

#Reset Button
reset_button = Button(text="Reset", font=("Arial", 15, "bold"), command=reset_timer)
reset_button.place(x=270, y=200)

#Label
check_label = Label(bg=BLUE, font=("Arial", 13))
check_label.place(x=20, y=0)



window.mainloop()


