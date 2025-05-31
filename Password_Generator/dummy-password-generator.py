'''SAMPLE PROGRAM USING TKINTER'''
# import tkinter as tk

# def button_click():
#     label.config(text="Button Clicked!")

# window = tk.Tk()
# window.title("Sample Tkinter Program")

# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack(pady=20)

# button = tk.Button(window, text="Click Me", command=button_click)
# button.pack()

# window.mainloop()




import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    
    chars = ""
    if use_letters.get():
        chars += string.ascii_letters
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Select at least one character type.")
        return
    
    password = "".join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Labels and Entry for password length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character types
use_letters = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=use_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).pack()

# Button to generate password
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Entry to display generated password
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Run the application
root.mainloop()