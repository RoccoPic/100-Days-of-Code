#titled gui
#text entry for miles
#is equal to X KM
#when hitting calculate you can see the conversion to km
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=100,pady=100)

text_box = Entry(width=10)
text_box.grid(column=1,row=0)

miles_txt = Label(text="Miles")
miles_txt.grid(column=2,row=0)

equal_to_txt = Label(text="is equal to")
equal_to_txt.grid(column=0,row=1)

km_txt = Label(text="Km")
km_txt.grid(column=2,row=1)

convert_text = Label(text=0)
convert_text.grid(column=1,row=1)

def conversion():
    convert_text["text"] = float(text_box.get()) * 1.609

calc_button = Button(text="Calculate",command=conversion)
calc_button.grid(column=1,row=2)


window.mainloop()
