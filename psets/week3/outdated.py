months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
def main():
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in date:
                month_text, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split()
                month = months.index(month_text) + 1
                day = int(day)
                year = int(year)
            else:
                continue
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except (ValueError, IndexError):
            continue
main()
