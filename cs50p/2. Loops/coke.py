def main():
    money = 50
    while money > 0:
        print(f"Amount Due: {money}")
        payment = int(input("Inster a coin: "))
        if payment in [5,10,25]:
            money -= payment
        else:
            print("invalid coin")
    print(f"change owed: {abs(money)}")





main()
