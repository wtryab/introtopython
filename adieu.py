def main():
    list = []
    while True:
        try:
            name = input("Name:")
        except:
            break
        else:
            list.append(name)
    size = len(list)
    for i in range(size):
        if i == 0 and i == size - 1:
            print(f"Adieu, adieu, to {list[i]}", end=" ")
        elif i == 0:
            print(f"Adieu, adieu, to {list[i]}", end=", ")
        elif i == size - 1:
            print(f"and {list[i]}")
        else:
            print(list[i], end=", ")


main()
