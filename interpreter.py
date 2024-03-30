def main():
    interpret(input("Expression: "))


def interpret(exp):
    arr = exp.split(" ")
    if arr[1] == "+":
        print(float(arr[0]) + float(arr[2]))
    if arr[1] == "-":
        print(float(arr[0]) - float(arr[2]))
    if arr[1] == "*":
        print(float(arr[0]) * float(arr[2]))
    if arr[1] == "/":
        print(float(arr[0]) / float(arr[2]))


main()
