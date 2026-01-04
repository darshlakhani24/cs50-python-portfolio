import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \b means "word boundary", so this matches "um" as a full word only
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
