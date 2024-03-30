import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip=ip.strip()
    if matches:=re.search(r"^([0-2]?\d?\d)\.([0-2]?\d?\d)\.([0-2]?\d?\d)\.([0-2]?\d?\d)$",ip):
        list=ip.split(".")
        for num in list:
            if int(num)>255 or int(num)<0:
                return False 
        return True
    return False
    
if __name__ == "__main__":
    main()