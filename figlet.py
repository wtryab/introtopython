import sys
import pyfiglet
import random

if len(sys.argv) == 1:
    print(pyfiglet.figlet_format(input("Input: ")))
elif len(sys.argv) == 3 and sys.argv[1] == "--font" or sys.argv[1] == "-f":
    if (
        sys.argv[2] == "slant"
        or sys.argv[2] == "rectangles"
        or sys.argv[2] == "alphabet"
    ):
        print(pyfiglet.figlet_format(input("Input: "), sys.argv[2]))
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
