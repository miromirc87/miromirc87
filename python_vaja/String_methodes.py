

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result =len(name)
#result = name.find("B")
#result = name.rfind("j")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()

#result = name.isdigit()
#print(result)

#result = name.isalpha()
#print(result)

#result = phone_number.count("-")
#phone_number = phone_number.replace("-", "" )
#print(phone_number)


#print(name)
#print(result)

#________________________________________________________________________

#VAJA

#1. username is no more then 12 characters  / len(up_ime) <,>,=, x:
#2. username must not contain spaces        / .find("x")
#3. username must not contain digits        / isalpha


username = input("Enter user name: ")
username.find(" ")


if len(username) > 12:    #The len() function returns an integer representing the number of items in the object.
    print("Sorry, you are not allowed to enter more than 12 characters.")
elif not username.find(" ") == -1:
    print("no spaces please.")
elif not username.isalpha():
    print("no numbers please.")
else:
    print(f"Hello {username}!")