def main():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                raise ValueError("Invalid fraction.")
            percentage = (x / y) * 100
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please try again.")
main()
