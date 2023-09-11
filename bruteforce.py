import itertools
import tkinter as tk
from tkinter import messagebox

def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Specify the file path for the common passwords file
common_passwords_file = "English.dic"

# Load common passwords from the file
common_passwords = load_common_passwords(common_passwords_file)

def brute_force_password_cracker(password, characters, max_length):
    for common_pass in common_passwords:
        if common_pass == password:
            return common_pass  # Password found in common passwords list

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess == password:
                return guess  # Password found in brute force

    return None  # Password not found

def crack_password():
    target_password = password_entry.get()
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 8

    cracked_password = brute_force_password_cracker(target_password, character_set, max_password_length)

    if cracked_password:
        result = f"Password cracked: {cracked_password}"
    else:
        result = "Password not found."

    # Show the result in a popup window
    messagebox.showinfo("Password Cracker Result", result)

# Create a Tkinter window
window = tk.Tk()
window.title("Password Cracker")

# Label and Entry for password input
password_label = tk.Label(window, text="Enter the target password:")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()

# Button to initiate the cracking process
crack_button = tk.Button(window, text="Crack Password", command=crack_password)
crack_button.pack()

# Start the Tkinter main loop
window.mainloop()




