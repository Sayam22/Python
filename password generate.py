import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def show_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be at least 1.")
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        password_var.set("Please enter a valid number.")

app = tk.Tk()
app.title("Password Generator")

password_var = tk.StringVar()

length_label = tk.Label(app, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=show_password)
generate_button.pack(pady=10)

password_label = tk.Label(app, textvariable=password_var, wraplength=300)
password_label.pack(pady=5)

app.mainloop()
