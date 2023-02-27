from tkinter import *

import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORD = ""
FRENCH_LIST = []
ENGLISH_WORD = ""
current_num = None
current_card = {}
#------Generate new word----
word_list = pandas.read_csv("./data/french_words.csv")
to_learn = word_list.to_dict(orient="records")
#print(french)
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(index_card, image=front_flash)
    canvas.itemconfig(vocab, text=current_card["French"],fill="#000000")
    canvas.itemconfig(top_text, text='French',fill="#000000")
    flip_timer = window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(index_card, image=back_flash)
    canvas.itemconfig(vocab, text=current_card["English"], fill="#FAFAEB")
    canvas.itemconfig(top_text, text='English', fill="#FAFAEB")

window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_flash = PhotoImage(file="./images/card_front.png")
back_flash = PhotoImage(file="./images/card_back.png")
index_card = canvas.create_image(400,258,image=front_flash)
top_text = canvas.create_text(400,150,text='French',font=("Ariel",40,"italic"))
vocab = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.pack()


wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.pack(side="left")

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.pack(side = "right")
next_card()
window.mainloop()