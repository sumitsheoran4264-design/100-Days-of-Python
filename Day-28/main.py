from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)

    #timer_text 00:00
    canvas.itemconfig(timer_text, text= "00:00")

    #title_label "Timer" 
    timer_label.config(text="Timer")

    #reset check_mark_label
    check_mark_label.config(text="")

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
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
        countdown(long_break_sec) 
    elif reps % 2 == 0:
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        countdown(short_break_sec)
    else:
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_mint = math.floor(count / 60)
    count_second =  count % 60 
    if count_second == 0:
        count_second = "00"
    elif count_second < 10:
        count_second = f"0{count_second}"
    
    canvas.itemconfig(timer_text, text= f"{count_mint}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark_label.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

 
#Window
window = Tk()
window.title("Interval")
window.config(padx=100,pady=50, bg=YELLOW, highlightthickness=0)

#timer label
timer_label = Label()
timer_label.config(text="Timer",  font=(FONT_NAME, 35, "bold"), fg=GREEN, bg= YELLOW)
timer_label.grid(column=1 ,row=0)





#Canvas
canvas = Canvas(width=200, height=224, bg= YELLOW)
tomato_image = PhotoImage(file="Day-28/tomato.png")
canvas.create_image(103 ,112, image=tomato_image)
timer_text = canvas.create_text(103, 130,text="00:00", fill="blue", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



# button
start_button = Button(text="Start", command= start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

#check mark label
check_mark_label = Label(fg= RED, bg= YELLOW)
check_mark_label.grid(column=1, row=4)

window.mainloop()   