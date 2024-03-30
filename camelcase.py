def snake_case(word):
    reword=""
    for i in range(len(word)):
        if word[i].isupper():
            reword+="_"+word[i].lower()
        else:
            reword+=word[i]
    return reword
def main():
    word=input("Enter camelCase: ")
    print("camelCase: ",word )
    print("snake_case: ",snake_case(word))
main()