import random
import sys
def guess(level):
    num=random.randint(1,level)
    while True:
        try: 
            user=int(input("Guess: "))
        except:
            pass
        else:
            if user ==num:
                print("Just Right!")
                sys.exit()
            elif user >num:
                print("Too Large!")
            else:
                print("Too small!")
            


def main():
    level=0
    while True:
        try:
            level=int(input("Level: "))
        except:
            pass
        else:
            if level >0:
                break
    guess(level)



main()