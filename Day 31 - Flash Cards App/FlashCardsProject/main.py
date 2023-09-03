import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_bg, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = tkinter.Tk()
window.title("Flash Cards")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=0, row=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=1, row=1)

next_card()

window.mainloop()