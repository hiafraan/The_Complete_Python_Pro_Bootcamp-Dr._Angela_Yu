import random
from typing import Text
import pandas
from tkinter import Button, Canvas, PhotoImage, Tk

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/tamil_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Tamil", fill="black")
    canvas.itemconfig(card_word, text=current_card["Tamil"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(height=526, width=800)
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))

right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()


window.mainloop()
