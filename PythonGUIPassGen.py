import random
from tkinter import *

def generate_password():
    characters = "abcdefghijklmnoprstuwyxzABCDEFGHIJKLMNOPRSTUWYXZ0123456789.,:'!@#$%^&*()_+"
    length = int(my_entry.get())
    if length > 0:
        password = ''
        for _ in range(length):
            password += random.choice(characters)
        password_label.config(text=password)
    else:
        password_label.config(text="Invalid password length")

root = Tk()
root.title("PasswordGenerator")
root.geometry("300x275")

lf = LabelFrame(root, text="Length of password")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Arial", 24))
my_entry.pack(pady=20, padx=20)

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = Label(root, text="", font=("Arial", 18))
password_label.pack(pady=20)

root.mainloop()
