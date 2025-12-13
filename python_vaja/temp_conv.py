from itertools import repeat

while True:
    unit = input("Enter themperature in Celsius or Fahrenheit (C/F):")


    if unit == "C":
        temp = float(input("Enter the temperature: "))
        temp = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit is: {temp}F")

    elif unit == "F":
        temp = float(input("Enter the temperature: "))
        temp = round((temp - 32) * 5 / 9, 1)
        print(f"The temperature in Celsius is: {temp}C")

    else:
        print(f"{unit} is Invalid input")

    repeat = input("Do you want to convert another temperature? (yes/no): ").lower()
    if repeat != "yes":
        print("Goodbye!")
        break