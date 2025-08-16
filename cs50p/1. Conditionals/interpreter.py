math = input("put the operation: ").strip()

num1 = int(math.split()[0])
operation = math.split()[1]
num2 = int(math.split()[2])
answer = 0

if operation == "+":
    answer = num1 + num2

elif operation == "-":
    answer = num1 - num2

elif operation == "*":
    answer = num1 * num2

elif operation == "/":
    answer = num1 / num2

print(float(answer))

