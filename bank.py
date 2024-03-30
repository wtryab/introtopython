def main():
    greeting=input("Greeting: ")
    if greeting.find("Hello")>=0:
        print("$0")
    elif greeting.find("h",0)==0 or greeting.find("H",0)==0:
        print("$20")
    else:
        print("$100")

main()