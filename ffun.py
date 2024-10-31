import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        include_special_chars = special_chars_var.get()
        
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation
            
        password = ''.join(random.choice(characters) for _ in range(length))
        
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for length.")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Password length input
tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkbox for including special characters
special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
special_chars_check.pack(pady=5)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry to display the generated password
result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

# Run the application
root.mainloop()
