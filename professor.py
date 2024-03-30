import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try: 
            level=int(input("Level: "))
        except:
                pass
        else: 
            if 1<=level<=3:
                return level

def generate_integer(level):
    score=0
    for i in range(10):
        if level == 1:
            x=random.randint(0,9)
            y=random.randint(0,9)
        elif level == 2:
            x=random.randint(10,99)
            y=random.randint(10,99)
        elif level == 3:
            x=random.randint(100,999)
            y=random.randint(100,999)
        count=1
        while True:
            answer=input(f"{x} + {y} = ")
            try:
                answer = int(answer)
            except:
                if count<3:
                    print("EEE")
                    count=count+1
                else:
                    print(f"{x} + {y} = {x+y}")
                    break
            else:
                if int(answer)==(x+y):
                    score=score+1
                    break
                elif count<3:
                    print("EEE")
                    count=count+1
                else:
                    print(f"{x} + {y} = {x+y}")
                    break
    print(f"Score: {score}")


if __name__ == "__main__":
    main()