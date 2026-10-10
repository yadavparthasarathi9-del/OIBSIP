# BMI Calculator - Task 2

Python Programming track, OIBSIP internship.

## What it does

Simple BMI calculator app with a GUI. You enter your name, weight and height, it calculates your BMI and tells you which category you fall in (Underweight / Normal / Overweight / Obese). Color changes based on result so it's easy to read at a glance.

Also saves every calculation to a local database so you can track how your BMI changes over time - just click "Show BMI Trend" and it'll plot a graph.

## Tools used

- Python
- tkinter for the GUI
- sqlite3 to store records
- matplotlib for the trend graph

## How to run it

First install matplotlib if you don't have it:

```
pip install matplotlib
```

Then just run:

```
python bmi_calculator_v2.py
```

A window will pop up. Fill in your details and hit calculate. It'll create a `bmi_records.db` file automatically the first time you run it - that's where your data gets stored.

## Things I added beyond the basic requirement

- Color coded results (green for normal, red for obese etc)
- Saves history per name so multiple people can use it
- Graph to see BMI trend over multiple entries
- Basic validation - won't let you enter negative numbers or non-numeric stuff

## Known limitations

- No way to delete old records from the GUI right now, you'd have to edit the db directly
- Graph needs at least 2 saved entries for the same name to actually show a trend line
