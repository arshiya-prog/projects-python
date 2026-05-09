from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(height=250, width=250)
window.config(padx=50, pady=50)

miles_input = Entry(width=5)
miles_input.focus()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_output = Label(text=0)
km_output.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

def miles_converter():
    km = float(miles_input.get()) * 1.60934
    km_output.config(text=km)
button = Button(text="Calculate", command=miles_converter)
button.grid(row=2, column=1)

window.mainloop()