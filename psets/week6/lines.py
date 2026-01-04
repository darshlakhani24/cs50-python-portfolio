import sys
import os
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    if not os.path.isfile(filename):
        sys.exit("File does not exist")
    with open(filename) as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        count += 1
    print(count)
if __name__ == "__main__":
    main()
