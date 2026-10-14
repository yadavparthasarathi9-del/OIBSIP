# Weather App - Task 4

Python Programming track, OIBSIP internship.

## What it does

A simple desktop weather app. Type in any city name and it shows the current temperature, how it actually feels, humidity, and wind speed. There's also a quick forecast section showing the next couple of hours and the next 5 days.

You can toggle between Celsius and Fahrenheit with one button.

## Tools used

- Python
- tkinter for the GUI
- requests to call the weather API
- OpenWeatherMap API for the actual weather data

## Setup

1. Get a free API key from [openweathermap.org](https://openweathermap.org/api) (sign up, go to API keys section, copy it). Takes a couple hours sometimes for the key to activate, so don't panic if it doesn't work instantly.

2. Install requests if you don't have it:
```
pip install requests
```

3. Open `weather_app.py` and replace this line with your actual key:
```python
API_KEY = "PUT_YOUR_API_KEY_HERE"
```

4. Run it:
```
python weather_app.py
```

## How to use it

Type a city name (e.g. "Delhi" or "London") and click Get Weather. Click the unit button to switch between C and F.

## Things I added beyond the basic requirement

- Hourly + 5 day forecast, not just current weather
- C/F toggle
- Error handling for wrong city names, no internet, and slow/timeout requests

## Known limitations

- Free tier API has a request limit per minute, shouldn't be an issue for normal use
- Forecast data comes in 3-hour blocks from the API so the "hourly" view isn't minute-by-minute
- Don't commit your real API key to a public repo - better to use a placeholder like I did, or an environment variable
