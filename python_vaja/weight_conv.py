weight = float(input("enter your weight: "))

while True:
    unit = input("Kilograms or Pounds (K or L): ").upper()


    if unit == "K":
        weight = weight * 2.205
        unit = "Lbs."
        print(f"your weight is: {weight} {unit}")
        break
    elif unit == "L":
        weight = weight / 2.205
        unit = "Kgs."
        print(f"your weight is: {round(weight, 1)} {unit}")
        break
    else:
        print(f"{unit} is not a valid unit")


