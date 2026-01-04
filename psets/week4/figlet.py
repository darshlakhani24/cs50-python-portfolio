import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input()
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        text = input()
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid font")
else:
    sys.exit("Invalid usage")
