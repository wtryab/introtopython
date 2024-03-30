import sys
from PIL import Image, ImageOps
def main():
    if len(sys.argv)==3:
        p1,e1=sys.argv[1].lower().split(".")
        p2,e2=sys.argv[2].lower().split(".")
        if not(e1=="jpg" or e1=="jpeg"or e1=="png"):
            if not(e2=="jpg" or e2=="jpeg"or e2=="png"):
                sys.exit("not a valid ext")
            sys.exit("not a valid ext")
        else:
            try:
                shirt=Image.open("shirt.png")
                picture=Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("DOES NOT EXIST")
            else:
                i= ImageOps.fit(picture, shirt.size)
                i.paste(shirt, mask = shirt)
                i.save(sys.argv[2])
    elif len(sys.argv)<3:
        sys.exit("Too few arguments")
    else:
        sys.exit("Too many arguments")
        


if __name__=="__main__":
    main()