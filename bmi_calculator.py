
# BMI Calculator - Task 2 (Python Track)
# made for OIBSIP internship
# basic tkinter app + sqlite to save records + matplotlib graph for trend

import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import matplotlib.pyplot as plt

db_name = "bmi_records.db"


def setup_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date_time TEXT
    )''')
    conn.commit()
    conn.close()


def add_record(name, weight, height, bmi, category):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        c.execute("INSERT INTO records (name, weight, height, bmi, category, date_time) VALUES (?,?,?,?,?,?)",
                  (name, weight, height, bmi, category, now))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("DB error", str(e))


def fetch_records(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT date_time, bmi FROM records WHERE name=? ORDER BY id", (name,))
    data = c.fetchall()
    conn.close()
    return data


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif bmi < 25:
        return "Normal", "green"
    elif bmi < 30:
        return "Overweight", "orange"
    else:
        return "Obese", "red"


# ---- GUI part ----
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("380x400")

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack(pady=5)

tk.Label(frame1, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame1)
name_entry.grid(row=0, column=1)

tk.Label(frame1, text="Weight (kg)").grid(row=1, column=0, padx=5, pady=5)
weight_entry = tk.Entry(frame1)
weight_entry.grid(row=1, column=1)

tk.Label(frame1, text="Height (m)").grid(row=2, column=0, padx=5, pady=5)
height_entry = tk.Entry(frame1)
height_entry.grid(row=2, column=1)

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=15)


def calc_bmi():
    name = name_entry.get().strip()
    w = weight_entry.get().strip()
    h = height_entry.get().strip()

    if name == "":
        messagebox.showwarning("Wait", "Enter your name first")
        return

    # check numeric
    try:
        w = float(w)
        h = float(h)
    except:
        messagebox.showerror("Error", "Weight and height should be numbers only")
        return

    if w <= 0 or h <= 0:
        messagebox.showerror("Error", "Values can't be negative or zero")
        return

    bmi_val = w / (h * h)
    bmi_val = round(bmi_val, 2)

    cat, clr = get_category(bmi_val)
    result_label.config(text=f"BMI = {bmi_val}  ({cat})", fg=clr)

    add_record(name, w, h, bmi_val, cat)


def show_graph():
    name = name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Wait", "Type the name to check trend")
        return

    rows = fetch_records(name)
    if len(rows) == 0:
        messagebox.showinfo("No data", "No previous record found for this name")
        return

    dates = [r[0] for r in rows]
    bmis = [r[1] for r in rows]

    plt.plot(dates, bmis, marker='o')
    plt.title(name + "'s BMI over time")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.show()


btn1 = tk.Button(root, text="Calculate BMI", command=calc_bmi, bg="#4CAF50", fg="white")
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Show BMI Trend", command=show_graph)
btn2.pack(pady=5)

tk.Label(root, text="data gets saved automatically after calculating", font=("Arial", 8)).pack(side="bottom", pady=10)

setup_db()
root.mainloop()
