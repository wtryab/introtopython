"""
#loops#
def main():
    meow(getnum())

def getnum():
    while True:
        num=int(input("number pls"))
        if num>0:
            return num

def meow(n):
    for _ in range(n):
        print("meow")

main()#"""
#arrays#
students=[
    {"name":"Wardah","age":"20"},
    {"name":"Maha","age":"22"},
    {"name":"Abeer","age":"18"}
]
"""for i in range(len(students)):
    print(i+1, students[i])"""
"""for student in students:
    print(student["name"], student["age"], sep="\t")"""

def main():
    print_brick(3,5)

def print_brick(row,column):
    for i in range(row):
        for j in range(column):
            print("#", end="")
        print("")
        
def print_column(n):
    print("#\n"*n,end="")

def print_row(n):
    print("?"*n)

main() 