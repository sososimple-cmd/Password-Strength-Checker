import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate score
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Determine strength based on score
    if score <= 2:
        return f"Weak ({score}/5)"
    elif score <= 4:
        return f"Moderate ({score}/5)"
    else:
        return f"Strong ({score}/5)"

def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")  # Set the window size

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter your password below:")
instruction_label.pack(pady=10)

# Add an entry field for the password
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Add a button to check the password strength
check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()