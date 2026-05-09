from tkinter import *

# Creating windows
window = Tk()
window.config(bg="pink")
window.minsize(width=500, height=500)
window.title("My First GUI Program")
window.config(padx=10, pady=10)

# Creating labels
label = Label(text="I am a Label", font=("Calibri", 24, "italic"))
label.config(text="LOL")
label["text"] = "hi"
label.pack(side="left")

# Creating buttons
def button_clicked():
    # label["text"] = "Button was clicked"
    label.config(text=f"{entry.get()}")
button = Button(text="Click me", command=button_clicked, background="blue", font="Menlo")
button.pack()

# Creating entries
entry = Entry(width=30)
# entry.focus()
entry.insert(END, string="Insert text")
print(entry.get())
entry.pack()

# Creating text boxes
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Insert multi-line input")
print(text.get("1.0", END))     # print 1--> 1st line; 0--> 0th char
text.pack()

# Creating spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=5, width=5, command=spinbox_used)
spinbox.pack()

# Creating scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, width=5, command=scale_used)
scale.pack(side="left")

# Creating checkbox
def checkbutton_used():     # prints 1 is On button is checked, otherwise prints 0
    print(checked_state.get())
checked_state = IntVar()    # variable to hold the checked state. 1 if on, 0 if off
checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checkbox.pack()

# Creating radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()      # variable to hold which button value is checked
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Creating listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=5, width=10)
fruits = ["Apple", "Mango", "Banana", "Kiwi", "Sweet Lime"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.place(x=0, y=0)

window.mainloop()

