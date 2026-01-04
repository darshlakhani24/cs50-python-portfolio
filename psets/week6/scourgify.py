import sys
import csv
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.exit(f"Could not read {input_file}")

    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            cleaned_rows = []

            for row in reader:
                last, first = row["name"].split(", ")
                cleaned_rows.append({"first": first, "last": last, "house": row["house"]})
    except Exception as e:
        sys.exit(f"Error reading {input_file}: {e}")

    try:
        with open(output_file, "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(cleaned_rows)
    except Exception as e:
        sys.exit(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    main()
