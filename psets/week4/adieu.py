import sys

names = []

try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

if len(names) == 1:
    farewell = f"Adieu, adieu, to {names[0]}"
elif len(names) == 2:
    farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
else:
    farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

print(farewell)
