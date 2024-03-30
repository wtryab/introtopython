import sys
import csv


def main():
    if len(sys.argv) == 3:
        file1, ext1 = sys.argv[1].split(".")
        file2, ext2 = sys.argv[2].split(".")
        if ext1 == "csv" and ext2 == "csv":
            try:
                f1 = open(sys.argv[1])
                f2 = open(sys.argv[2], "w", newline="")
            except FileNotFoundError:
                sys.exit("File DOES NOT EXIST")
            else:
                names = []
                firstnames = []
                lastnames = []
                house = []
                string = csv.DictReader(f1)
                for rows in string:
                    names.append(rows["name"])
                    house.append(rows["house"])
                for fullname in names:
                    l, f = str(fullname).split(",")
                    f = f.strip()
                    firstnames.append(f)
                    lastnames.append(l)
                data = []
                for i in range(len(house)):
                    data.append(
                        dict(
                            firstname=firstnames[i],
                            lastname=lastnames[i],
                            house=house[i],
                        )
                    )
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(f2, fieldnames=fieldnames)
                writer.writeheader()
                for i in range(len(house)):
                    writer.writerow(
                        {
                            "first": firstnames[i],
                            "last": lastnames[i],
                            "house": house[i],
                        }
                    )
                f1.close()
                f2.close()
        else:
            sys.exit("NOT CSV FILE")

    elif len(sys.argv) < 3:
        sys.exit("Not enough arguments")
    else:
        sys.exit("Too many arguments")


main()
