import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$'
    match = re.match(pattern, ip)
    if not match:
        return False
    for part in match.groups():
        if not 0 <= int(part) <= 255:
            return False
    return True

if __name__ == "__main__":
    main()
