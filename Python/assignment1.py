num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2

elif operation == '-':
    result = num1 - num2

elif operation == '*':
    result = num1 * num2

elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2

else:
    print("Invalid operation. Please enter +, -, *, or /.")
    result = None

if result is not None:
    print(f"{num1} {operation} {num2} = {result}")