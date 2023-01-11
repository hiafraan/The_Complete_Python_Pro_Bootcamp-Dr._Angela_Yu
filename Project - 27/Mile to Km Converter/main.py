from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)


label2 = Label(text="Miles")
label2.grid(column=2, row=0)


label3 = Label(text="Km")
label3.grid(column=2, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
