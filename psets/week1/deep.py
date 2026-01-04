def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    if answer == "42" or answer == "forty-two" or answer == "Forty Two" or answer== "forty two" or answer== "FoRty TwO":
        print("Yes")
    else:
        print("No")
main()
