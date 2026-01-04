def main():
    camel = input("camelCase: ")
    snake = ""
    i = 0
    for j in range(len(camel)):
        if camel[j].isupper():
            snake += camel[i:j] + "_" + camel[j].lower()
            i = j + 1
    snake += camel[i:]
    print("snake_case:", snake)
main()
