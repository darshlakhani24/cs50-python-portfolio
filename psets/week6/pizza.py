import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            table = [row for row in reader]
    except Exception:
        sys.exit("Could not read the file")

    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
