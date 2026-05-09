from tkinter import *

window = Tk()
window.minsize(height=300, width=500)
window.title("Challenge")
window.config(padx=10, pady=10)

label = Label(text="Sample label", font=("Menlo", 26, "bold"))
label.grid(row=0, column=0)

def button_used():
    print("Button clicked")
button1 = Button(text="Is on?", command=button_used)
button1.grid(row=1, column=1)

button2 = Button(text="2nd Button", command=button_used)
button2.grid(row=0, column=2)

entry = Entry(width=10)
entry.focus()
entry.insert(END, string="Insert text")
entry.grid(row=2, column=3)

window.mainloop()