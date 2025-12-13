
operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
        result = num1 + num2
        print("Result:", result)
elif operator == "-":
        result = num1 - num2
        print("Result:", result)
elif operator == "*":
        result = num1 * num2
        print("Result:", result)
elif operator == "/":
        result = num1 / num2
        print("Result:", result)
else:
    print(f'"{operator}" is Invalid operator')

