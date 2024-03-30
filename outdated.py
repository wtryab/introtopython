list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert1(date):
    month,day,year=date.split("/")
    print(month,day,year,sep="  ")
    if int(month)>12 or int(month)<0:
        return Exception(ValueError)
    if int(day)>31 or int(day)<28:
        return ValueError
    if int(month)<10:
        month="0"+str(month)
    if int(day) <10:
        day="0"+str(day)
    print(f"{year}-{month}-{day}")

def convert2(date):
    month,day,year=date.split(" ")
    print(month,day,year,sep="  ")
    day=int(day.strip(","))
    month=list.index(month)+1
    if month<10:
        month="0"+str(month)
    if day<10:
        day="0"+str(day)
    print(f"{year}-{month}-{day}")

def main():
    while True:
        date=input("Date: ").strip()
        try:
            if date.find("/")>=0:
                convert1(date)
                break
            if date.find(" ")>=0:
                convert2(date)
                break
        except ValueError:
            pass

main()
