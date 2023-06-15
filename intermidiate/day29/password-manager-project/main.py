from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_input.delete(0, "end")
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == "" or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_input.get().title()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Data file is not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No detail for the {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Times New Roman", 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Times New Roman", 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password", font=("Times New Roman", 12))
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "yourmail@mail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", font=("Times New Roman", 10), command=generate_password)
generate_pass_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", font=("Times New Roman", 10), width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", font=("Times New Roman", 10), width=15, command=search_password)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()
