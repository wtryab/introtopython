def main():
    print(value(input("Greeting")))

def value(greeting):
    if greeting.find("Hello")>=0:
        return ("$0")
    elif greeting.find("h",0)==0 or greeting.find("H",0)==0:
        return ("$20")
    else:
        return("$100")

if __name__ == "__main__":
    main()