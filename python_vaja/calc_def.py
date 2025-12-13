ops={"+": lambda a,b: a+b}

while True:
    operator = input ("enter + operator: ")
    if operator in ops:
        break
    print("wrong operator")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("Result:", ops[operator](a,b))

