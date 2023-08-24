import tkinter
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                #Creating json file
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

# ------------------------- FIND PASSWORD ----------------------------- #
def find_password():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = website_entry.get()
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Login Details", message=f"Email: {email}\n"
                                                               f"Password: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Lables
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = tkinter.Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tkinter.Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "milosz@email.com")

password_entry = tkinter.Entry(width=33)
password_entry.grid(column=1, row=3)

#Buttons
generate_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=43, command=save_password)
add_button.grid(columnspan=2, column=1, row=4)

search_button = tkinter.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)




window.mainloop()