def main():
    time=input("What time is it: ") 
    convert(time)

def convert(time):
    hours,mins=time.split(":")
    hours=int(hours)
    mins=float(mins)/60
    if hours==7 or hours==8:
        print("breakfast time")
    elif hours==12 or hours==13:
        print("lunch time")
    if hours==18 or hours==19:
        print("dinner time")
    else:
        print()
    return hours+mins

if __name__ == "__main__":
    main()
    