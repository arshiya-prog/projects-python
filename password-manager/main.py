import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json
import string

FILE_PATH_JSON = "/Users/arshiya/Desktop/Coding/Python/Python_Projects/password-manager/data.json"
FILE_PATH = "/Users/arshiya/Desktop/Coding/Python/Python_Projects/password-manager/data.txt"
IMAGE_PATH = "/Users/arshiya/Desktop/Coding/Python/Python_Projects/password-manager/logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    password = []

    letters = [chr(idx) for idx in range(97, 123)]
    for idx in range(65, 91):
        letters.append(chr(idx))
    symbols = [chr(idx) for idx in range(35, 39)]

    password_l = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_s = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_n = [str(random.randint(0, 9)) for _ in range(random.randint(2, 4))]

    password = password_l+password_n+password_s

    random.shuffle(password)
    password = "".join(password)

    password_entry.insert(tk.END, string=password)

    pyperclip.copy(text=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")

    else:
        # confirmation = messagebox.askokcancel(title=website, message="Details entered-"
        #                                     f"\nEmail: {email}\nPassword: {password}"
        #                                     "\n\nIs it okay to save?")
        # if confirmation == True:

        try:
            with open(FILE_PATH_JSON, "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(FILE_PATH_JSON, "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open(FILE_PATH_JSON, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # data.writelines(f"{website} | {email} | {password}\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    pascal_website = string.capwords(website)
    try:
        with open(FILE_PATH_JSON, "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if pascal_website in data:
            email = data[pascal_website]['email']
            password = data[pascal_website]['password']
            messagebox.showinfo(title= website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {pascal_website} found.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = tk.Canvas(height=200, width=200, highlightthickness=0)
image_path = tk.PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 100, image=image_path)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=11, command=search_password)
search_button.grid(row=1, column=2)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(tk.END, string="name@email.com")

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=33, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()