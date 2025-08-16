bucks = input("greeting: ")
bucks = bucks.strip()
bucks = bucks.lower()


if bucks[0:5]  == "hello":
    print("$0")

elif bucks [0] == "h":
    print("$20")

else:
    print("$100")
