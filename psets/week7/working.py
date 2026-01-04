import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, ampm1, h2, m2, ampm2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (0 <= m1 < 60 and 0 <= m2 < 60):
        raise ValueError("Invalid minutes")
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError("Invalid hour")

    time1 = to_24_hour(h1, m1, ampm1)
    time2 = to_24_hour(h2, m2, ampm2)

    return f"{time1} to {time2}"

def to_24_hour(hour, minute, period):
    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:  # PM
        hour = hour if hour == 12 else hour + 12
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()