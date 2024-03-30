list={}
def main():
    while True:
        try:
            item=input().upper()
            total=list.get(item)
            if total == None:
                list[item]=1
            else:
                list[item]=total+1
        except EOFError or TypeError or ValueError:
            break
    sortedlist=dict(sorted(list.items()))
    for key,value in sortedlist.items():
        try:
            print(value, key)
        except:
            return 0


main()