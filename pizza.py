import csv
import sys
from tabulate import tabulate

if len(sys.argv) == 2:
    file, ext = sys.argv[1].split(".")
    if ext == "csv":
        try:
            actual_file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File Not Found")
        else:
            lines = csv.reader(actual_file)
            for row in lines:
                header = row
                break
            print(tabulate(lines, headers=header, tablefmt="grid"))
    else:
        sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many Command-Line arguments")
else:
    sys.exit("Too few Command-Line arguments")
