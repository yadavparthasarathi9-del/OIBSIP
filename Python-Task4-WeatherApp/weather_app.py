
# Weather App - Task 4 (Python Track)
# OIBSIP internship
# tkinter GUI + OpenWeatherMap API, shows current weather + hourly/daily forecast

import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "0bb8e37ad5d25fd5fc0eb5bf6706a7db"   # openweathermap.org key

root = tk.Tk()
root.title("Weather App")
root.geometry("400x480")

tk.Label(root, text="Weather App", font=("Arial", 18, "bold")).pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack(pady=5)

tk.Label(frame1, text="City:").grid(row=0, column=0, padx=5)
city_entry = tk.Entry(frame1, width=20)
city_entry.grid(row=0, column=1)

unit = tk.StringVar(value="metric")  # metric = C, imperial = F


def toggle_unit():
    if unit.get() == "metric":
        unit.set("imperial")
        unit_btn.config(text="Switch to °C")
    else:
        unit.set("metric")
        unit_btn.config(text="Switch to °F")
    if city_entry.get().strip() != "":
        get_weather()


main_frame = tk.Frame(root)
main_frame.pack(pady=15)

city_label = tk.Label(main_frame, text="", font=("Arial", 14, "bold"))
city_label.pack()

temp_label = tk.Label(main_frame, text="", font=("Arial", 32))
temp_label.pack()

desc_label = tk.Label(main_frame, text="", font=("Arial", 12))
desc_label.pack()

details_label = tk.Label(main_frame, text="", font=("Arial", 10), justify="left")
details_label.pack(pady=10)

forecast_frame = tk.Frame(root)
forecast_frame.pack(pady=10)

forecast_label = tk.Label(forecast_frame, text="", font=("Arial", 9), justify="left")
forecast_label.pack()


def get_weather():
    city = city_entry.get().strip()
    if city == "":
        messagebox.showwarning("Wait", "Type a city name first")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit.get()}"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"].title()
        name = data["name"]
        country = data["sys"]["country"]

        deg = "°C" if unit.get() == "metric" else "°F"

        city_label.config(text=f"{name}, {country}")
        temp_label.config(text=f"{temp}{deg}")
        desc_label.config(text=desc)
        details_label.config(
            text=f"Feels like: {feels}{deg}\nHumidity: {humidity}%\nWind speed: {wind} m/s"
        )

        get_forecast(city)

    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Request timed out, try again")
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "No internet connection")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


def get_forecast(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={unit.get()}"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            return

        deg = "°C" if unit.get() == "metric" else "°F"
        lines = ["Next hours:"]
        # api gives data in 3 hour steps, grab first 2 for ~6hr forecast
        for item in data["list"][:2]:
            time_txt = item["dt_txt"].split(" ")[1][:5]
            t = item["main"]["temp"]
            lines.append(f"  {time_txt} - {t}{deg}")

        lines.append("\nNext days:")
        seen_dates = set()
        for item in data["list"]:
            date_txt = item["dt_txt"].split(" ")[0]
            time_txt = item["dt_txt"].split(" ")[1]
            if time_txt == "12:00:00" and date_txt not in seen_dates:
                seen_dates.add(date_txt)
                t = item["main"]["temp"]
                lines.append(f"  {date_txt} - {t}{deg}")
            if len(seen_dates) >= 5:
                break

        forecast_label.config(text="\n".join(lines))

    except Exception:
        forecast_label.config(text="(forecast unavailable)")


btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

get_btn = tk.Button(btn_frame, text="Get Weather", command=get_weather, bg="#2980b9", fg="white")
get_btn.grid(row=0, column=0, padx=5)

unit_btn = tk.Button(btn_frame, text="Switch to °F", command=toggle_unit)
unit_btn.grid(row=0, column=1, padx=5)

root.mainloop()
