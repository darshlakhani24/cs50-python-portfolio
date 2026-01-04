# Bill Splitter Program

def get_total_bill():
    # Prompts the user to enter the total bill amount.
    # Keeps prompting until a valid positive number is entered.
    while True:
        try:
            total = float(input("Enter the total bill amount (₹): "))
            if total > 0:
                return total
            else:
                print("Bill amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_people():
    # Prompts the user to enter names separated by commas.
    # Allows quitting by typing 'q'. Return a list of names.
    while True:
        names = input("Enter names of people separated by commas (or type 'q' to quit): ").strip()
        if names.lower() == 'q':
            print("Exiting program. Goodbye!")
            exit()
        people = [name.strip().capitalize() for name in names.split(",") if name.strip()]
        if people:
            return people
        else:
            print("Please enter at least one name.")


def tip(amount, tip_percent):
    # Calculates the total amount after adding tip.
    # Returns the updated total rounded to 2 decimal places.
    tip_amount = (tip_percent / 100) * amount
    return round(amount + tip_amount, 2)


def split_equal(total, people):
    # Splits the total bill equally among all people.
    # Returns a dictionary mapping names to their equal share.
    share = round(total / len(people), 2)
    return {person: share for person in people}


def split_custom(total, people):
    # Allows users to enter how much each person wants to contribute.
    # Automatically calculates the last person’s contribution to balance the bill.
    # Returns a dictionary with the contributions.
    contributions = {}
    running_total = 0

    for i, person in enumerate(people):
        if i == len(people) - 1:
            # Automatically assigns the last person the remaining balance
            final_share = round(total - running_total, 2)
            contributions[person] = final_share
            print(f"{person} will pay ₹{final_share} to complete the bill.")
            break

        while True:
            try:
                amount = float(input(f"Enter contribution for {person} (₹): "))
                if amount < 0:
                    print("Contribution cannot be negative.")
                elif running_total + amount > total:
                    print(f"Total would exceed ₹{total}. You can only contribute ₹{round(total - running_total, 2)} or less.")
                else:
                    contributions[person] = round(amount, 2)
                    running_total += amount
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return contributions


def generate_summary(split, total):
    # Generates a summary of contributions and the total bill.
    # Returns a formatted string showing each person's amount and total.
    summary = "\n----- Payment Summary -----\n"
    for person, amount in split.items():
        summary += f"{person} owes ₹{amount}\n"
    summary += f"Total Bill: ₹{total}"
    return summary


def main():
    # Main function to control the overall flow of the bill splitter program.

    print("Welcome to the Bill Splitter!")

    # Step 1: Get the total bill amount
    total = get_total_bill()

    # Step 2: Ask the user if they want to add a tip
    while True:
        add_tip = input("Would you like to add a tip? (y/n): ").strip().lower()
        if add_tip in ['yes', 'y']:
            while True:
                try:
                    tip_percent = float(input("Enter tip percentage (e.g., 10 for 10%): "))
                    if tip_percent >= 0:
                        total = tip(total, tip_percent)
                        print(f"New total with tip: ₹{total}")
                        break
                    else:
                        print("Tip percentage cannot be negative.")
                except ValueError:
                    print("Please enter a valid number.")
            break
        elif add_tip in ['no', 'n']:
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

    # Step 3: Get the list of people
    people = get_people()

    # Step 4: Ask how to split the bill (equal or custom)
    while True:
        method = input("Do you want to split the bill equally or by custom contributions? (equal/custom): ").strip().lower()
        if method == "equal":
            split = split_equal(total, people)
            break
        elif method == "custom":
            split = split_custom(total, people)
            break
        else:
            print("Invalid choice. Please type 'equal' or 'custom'.")

    # Step 5: Display the final summary
    print(generate_summary(split, total))


if __name__ == "__main__":
    main()
