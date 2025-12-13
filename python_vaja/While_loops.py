#While loop= execute some code While some conditions remains true


#1_____Primer____________________________________________

name = input("Enter your name: ")


while name =="":
    print("Please enter a name")
    name = input("Enter your name: ")

else:
    print(f"hello {name}")


#2______Primer__________________________________________


age = int(input("Enter your age: "))

while age < 0:
    print("Please enter a valid age")
    age = input("Enter your age: ")

print(f"your age is {age}")

#3______Primer_______________________________________________

food = input("Enter your food (q to quit): ")

while not food.lower =="q":
    print(f"you like {food}")
    food = input("Enter another food (q to quit): ")

print("bye")

#4_____Primer______________________________________________


num = int(input("Enter a number 1-10: "))

while num < 1 or num > 10:
    print (f"{num} is not a valid number")
    num = int(input("Enter a # between 1 and 10: "))

print(f"your number is {num}")

