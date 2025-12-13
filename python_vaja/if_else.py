#   age = int(input("Enter your age: "))

#   if age >= 18:
#        print("You are old enough")

#   elif age <= 0:
#        print("You are not born")

#   else:
#        print("You are NOT old enough!")





while True:
    response = input("wuld you like food? (y/n):")

    if response == "y":
        print("here you go")
        break
    elif response == "n":
        print("no food for you then.")
        break
    else:
        print("didnt get that??? (y or n)")

while True:
    name = input("Enter your name: ")

    if name == "":
        print("no name entered")
    else:
        print(f"hello {name}")
        break



online = True

if online:
    print("online")
else:
    print("offline")
