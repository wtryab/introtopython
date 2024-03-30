import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    timesystem="(?:(\d{1,2}):(\d{1,2})|(\d{1,2})) (AM|PM)"
    if time:=re.search(rf"{timesystem} to {timesystem}",s):
        count=0
        for i in range(len(time.groups())):
            if time.group(i+1):
                count=count+1
        if count==6:
            shours,sminutes,smeridien=time.group(1,2,4)
            ehours,eminutes,emeridien=time.group(5,6,8)
            if smeridien=="PM":
                shours=12+int(shours)
                
            if smeridien=="PM":
                shours=12+int(shours)
                
            if emeridien=="PM":
                ehours=12+int(ehours)
            return (f"{shours}:{sminutes} to {ehours}:{eminutes}")

        elif count==4:
            shours,smeridien=time.group(3,4)
            ehours,emeridien=time.group(7,8)

if __name__ == "__main__":
    main()