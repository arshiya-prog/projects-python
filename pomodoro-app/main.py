import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS 
    work_min = WORK_MIN*60
    short_break_min = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60

    REPS += 1
    if REPS % 8 == 0:
        countdown(long_break_min)
        label.config(text="Break", fg=RED)
    elif REPS%2 == 0:
        countdown(short_break_min)
        label.config(text="Break", fg=PINK)
    elif REPS%2 != 0:
        countdown(work_min)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    cm = ""
    minute = count//60
    sec = count % 60
    if minute < 10:
        minute = f"0{minute}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count>0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        start_timer()
        work_sesh = REPS//2
        for _ in range(work_sesh):
            cm += "✔"
        checkmark.config(text=cm)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # height and width of the image you wanna insert
tomato_img_path = tk.PhotoImage(file="/Users/arshiya/Desktop/Coding/Python/Python_Projects/pomodoro-app/tomato.png")
canvas.create_image(100, 112, image=tomato_img_path)    # generates the image
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25))    # creates the text in front of the image
canvas.grid(row=1, column=1)

label = tk.Label(text="Timer", font=("Courier", 35), bg=YELLOW, fg=GREEN)
label.config()
label.grid(row=0, column=1)

start_button = tk.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = tk.Label(fg=GREEN, bg=YELLOW, font=("", 20))
checkmark.grid(row=3, column=1)

window.mainloop()