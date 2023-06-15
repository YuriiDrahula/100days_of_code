from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv(".\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(".\\data\\french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(background_image, image=card_front_image)
    canvas.itemconfig(title, fill="black", text="French")
    canvas.itemconfig(word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(background_image, image=card_back_image)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=current_card["English"])


def is_known():
    words.remove(current_card)
    new_data = pandas.DataFrame(words)
    new_data.to_csv(".\\data\\words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file=".\\images\\card_front.png")
card_back_image = PhotoImage(file=".\\images\\card_back.png")
background_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons
right_image = PhotoImage(file=".\\images\\right.png")
wrong_image = PhotoImage(file=".\\images\\wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
