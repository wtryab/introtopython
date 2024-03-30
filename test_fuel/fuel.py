def main():
    convert(input("Fraction:"))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x < y:
            percentage = round(x / y * 100)
            return gauge(percentage)
    except ValueError or ZeroDivisionError:
        print("zero")
        pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
