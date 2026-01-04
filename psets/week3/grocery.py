def main():
    items = {}
    while True:
        try:
            item = input().strip().lower()
            if item:
                items[item] = items.get(item, 0) + 1
        except EOFError:
            print()
            break
    for item in sorted(items):
        print(f"{items[item]} {item.upper()}")
main()
