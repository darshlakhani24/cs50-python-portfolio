def get_input():
    return input("Item: ")
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.0
    running = True
    while running:
        try:
            item = get_input().strip().title()
        except EOFError:
            running = False
            print()
            continue
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
main()
