import sys
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)==2:
        file=sys.argv[1]
        ext=file.split(".")
        if not(ext[1]=="py"):
            sys.exit("Not a python file")
        try:
            act_file=open(file)
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            nospacelines=[]
            lines=act_file.readlines()
            for i in range(len(lines)):
                if not(lines[i]=='\n') and not(lines[i].find("#")>=0):
                    nospacelines.append(lines[i])
            print(len(nospacelines))
            act_file.close()
    else:
        sys.exit("Too many command-line arguments")    

if __name__=="__main__":
    main()