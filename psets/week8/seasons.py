from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of Birth (YYYY-MM-DD): ")
    try:
        minutes = get_minutes_since_birth(birthdate)
        words = p.number_to_words(round(minutes), andword="").capitalize()
        print(f"{words} minutes")
    except:
        sys.exit("Invalid date")

def get_minutes_since_birth(dob):
    try:
        year, month, day = map(int, dob.split("-"))
        birth = date(year, month, day)
        today = date.today()
        delta = today - birth
        minutes = delta.days * 24 * 60
        return minutes
    except ValueError:
        raise

if __name__ == "__main__":
    main()
