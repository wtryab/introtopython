def main():
    shorten(input("Word:"))

def shorten(word):
    word=word.strip()
    arr=[
        "A",
        "E",
        "I",
        "O",
        "U",
        "a",
        "e",
        "i",
        "o",
        "u",

    ]
    for i in range (len(arr)):
        word=word.replace(arr[i],"")
    return word

if __name__ == "__main__":
    main()
