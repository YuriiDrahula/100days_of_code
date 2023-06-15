from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=200, width=350)
window.config(padx=40, pady=40)


# Is equal to label
is_equal_label = Label()
is_equal_label.config(text="is equal to", font=("Arial", 16))
is_equal_label.grid(column=0, row=1)


# Input field
input = Entry(width=10)
input.grid(column=1, row=0)


# Miles, km, result labels
miles_label = Label()
miles_label.config(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

km_label = Label()
km_label.config(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)

result = Label(text=0, font=("Arial", 16))
result.grid(column=1, row=1)


# Calculate button
def convert():
    km = round(float(input.get()) * 1.609, 2)
    result.config(text=km)


button = Button(text="Calculate", font=("Arial", 12), command=convert)
button.grid(column=1, row=2)


window.mainloop()