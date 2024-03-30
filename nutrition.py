def main():
    item=calorie(input("Item: "))
    if item !="":
        print("Calories:",item)

def calorie(item):
    item=item.lower().strip()
    match(item):
        case "apple":
            return 130
        case "avocado":
            return 50
        case "sweet cherries":
            return 100
        case "banana":
            return 110
        case "kiwifruit":
            return 90
        case "pear":
            return 100
        case _ :
            return ""

main()