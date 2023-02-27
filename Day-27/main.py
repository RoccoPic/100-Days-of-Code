from tkinter import *

window = Tk() #need a way of keeping the window on the screen
window.title("First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=20,pady=20) #adds more space for our widgets

#Label
my_label = Label(text="taco",font =("Papyrus",20))
my_label["text"] = "cat"
my_label.config(text="tacocat")
my_label.config(padx=50,pady=50)
my_label.grid(column=0,row=0) #packs our label onto the screen


#button
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

#Entry
input = Entry(width = 10)
input.grid(column=3,row=2)
print(input.get())

button = Button(text="No Click me",command=button_clicked)
button.grid(column=2,row=0)












#keeps our window on the screen
window.mainloop()