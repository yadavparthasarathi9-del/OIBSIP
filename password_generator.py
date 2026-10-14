
# Password Generator - Task 3 (Python Track)
# OIBSIP internship
# tkinter GUI, uses secrets module for actually random/secure passwords
# strength meter + copy to clipboard + history of last few generated

import tkinter as tk
from tkinter import messagebox
import string
import secrets

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x480")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# ---- length ----
frame1 = tk.Frame(root)
frame1.pack(pady=5)

tk.Label(frame1, text="Length:").grid(row=0, column=0, padx=5)
length_var = tk.IntVar(value=12)
length_entry = tk.Entry(frame1, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1)

# ---- character type checkboxes ----
frame2 = tk.Frame(root)
frame2.pack(pady=10)

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)
avoid_ambiguous = tk.BooleanVar(value=False)

tk.Checkbutton(frame2, text="Uppercase (A-Z)", variable=use_upper).pack(anchor="w")
tk.Checkbutton(frame2, text="Lowercase (a-z)", variable=use_lower).pack(anchor="w")
tk.Checkbutton(frame2, text="Numbers (0-9)", variable=use_digits).pack(anchor="w")
tk.Checkbutton(frame2, text="Symbols (!@#$...)", variable=use_symbols).pack(anchor="w")
tk.Checkbutton(frame2, text="Avoid ambiguous chars (0, O, l, 1)", variable=avoid_ambiguous).pack(anchor="w")

# ---- result display ----
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Consolas", 13), justify="center", state="readonly")
result_entry.pack(pady=10, padx=20, fill="x")

strength_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
strength_label.pack()

history = []  # keeps last 5 generated passwords, not saved to any file


def check_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if len(pw) >= 12:
        score += 1
    if any(c.isupper() for c in pw) and any(c.islower() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in string.punctuation for c in pw):
        score += 1

    if score <= 2:
        return "Weak", "red"
    elif score <= 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"


def generate_password():
    try:
        length = int(length_var.get())
    except (ValueError, tk.TclError):
        messagebox.showerror("Error", "Length must be a number")
        return

    if length < 4:
        messagebox.showwarning("Too short", "Minimum length is 4")
        return
    if length > 64:
        messagebox.showwarning("Too long", "Keep it under 64 characters")
        return

    pool = ""
    if use_upper.get():
        pool += string.ascii_uppercase
    if use_lower.get():
        pool += string.ascii_lowercase
    if use_digits.get():
        pool += string.digits
    if use_symbols.get():
        pool += string.punctuation

    if pool == "":
        messagebox.showwarning("Wait", "Select at least one character type")
        return

    if avoid_ambiguous.get():
        for ch in "0Ol1I":
            pool = pool.replace(ch, "")

    # using secrets instead of random - actually meant for passwords/security stuff
    pw = "".join(secrets.choice(pool) for _ in range(length))

    result_var.set(pw)
    strength, color = check_strength(pw)
    strength_label.config(text=f"Strength: {strength}", fg=color)

    history.insert(0, pw)
    if len(history) > 5:
        history.pop()
    update_history_box()


def copy_password():
    pw = result_var.get()
    if pw == "":
        messagebox.showwarning("Nothing to copy", "Generate a password first")
        return
    root.clipboard_clear()
    root.clipboard_append(pw)
    messagebox.showinfo("Copied", "Password copied to clipboard")


def update_history_box():
    history_box.config(state="normal")
    history_box.delete("1.0", tk.END)
    for p in history:
        history_box.insert(tk.END, p + "\n")
    history_box.config(state="disabled")


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

gen_btn = tk.Button(btn_frame, text="Generate Password", command=generate_password, bg="#2980b9", fg="white")
gen_btn.grid(row=0, column=0, padx=5)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_password)
copy_btn.grid(row=0, column=1, padx=5)

tk.Label(root, text="Last 5 generated (this session only):", font=("Arial", 9)).pack(pady=(15, 0))

history_box = tk.Text(root, height=5, width=35, font=("Consolas", 9), state="disabled")
history_box.pack(pady=5)

root.mainloop()
