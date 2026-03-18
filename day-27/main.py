import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("My First GUI Program")

label = tkinter.Label(text="I am a Label", font=("Calibri", 24, "italic"))
label.pack()

window.mainloop()

