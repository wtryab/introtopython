def main():
    while True:
        try:
            x,y=input("Fraction:").split("/")
            x=int(x)
            y=int(y)

            if x>y:
                continue
            else:
                per=(round(x/y*100))
                if per>=99:
                    print("F")
                elif per<=1:
                    print("E")
                else:
                    print(f"{per}%")
                break
        except ValueError or ZeroDivisionError:
            print("zero")
            pass

main()             