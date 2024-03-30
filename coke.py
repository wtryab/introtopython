def main():
    coke=50
    total=0
    while coke>=0:
        print("Amount Due:",coke)
        coin=int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin ==5: 
            coke-=coin
            total+=coin
        if coke<=0:
            print("Change Owed:",total-50 )
            break

main()