num1 = int(float(input("Enter first number: ")))
num2 = int(float(input("Enter second number: ")))

operator = input("Enter a operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator")