# Password Generator - Task 3

Python Programming track, OIBSIP internship.

## What it does

Generates random passwords based on what you pick - length, and which character types to include (uppercase, lowercase, numbers, symbols). Shows a quick strength rating (Weak/Medium/Strong) and lets you copy the password with one click.

Also keeps the last 5 passwords generated in this session so you can scroll back if you generated something better a minute ago.

## Tools used

- Python
- tkinter for the GUI
- secrets module (not random) for actually generating the passwords - this matters because `random` isn't meant for anything security related, `secrets` is designed for it

## How to run it

```
python password_generator.py
```
No extra installs needed, everything used is part of standard Python.

## How to use it

1. Set your desired length (default 12)
2. Check/uncheck which character types you want included
3. Optionally turn on "Avoid ambiguous chars" if you don't want confusing characters like 0/O or l/1 in there
4. Click Generate
5. Click Copy to put it on your clipboard

## Things I added beyond the basic requirement

- Strength meter (color coded)
- Copy to clipboard button
- Option to exclude ambiguous looking characters
- History of last 5 passwords from the session
- Validation so you can't generate with 0 character types selected or a silly length

## Known limitations

- History is only kept while the app is open, nothing is saved to a file (on purpose - don't want to write passwords to disk)
- Minimum length is 4, didn't see a point going lower than that
