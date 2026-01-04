def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    return (
        length_is_valid(s)
        and starts_with_two_letters(s)
        and has_valid_characters(s)
        and numbers_at_end(s)
    )
def length_is_valid(s):
    return 2 <= len(s) <= 6
def starts_with_two_letters(s):
    return s[:2].isalpha()
def has_valid_characters(s):
    return s.isalnum()
def numbers_at_end(s):
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                if char == '0':
                    return False
                number_started = True
        elif number_started:
            return False
    return True
main()
