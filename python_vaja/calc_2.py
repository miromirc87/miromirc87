def plus(a,b):
    return a + b

ops={"+":plus}

while True:
    operator=input("set the operator +: ")
    if operator in ops:
        break
    print("wrong operator")

a=input("first number: ")
b=input("second number: ")

print("result:", ops[operator](a,b),(" Bravooo!"))

