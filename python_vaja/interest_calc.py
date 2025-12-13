principle = 5000 #0
rate = 2         #0
time = 5         #0


#1________Primer________________________________________________

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be less then or equal to zero")


while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate cant be less then or equal to zero")


while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time cant be less then or equal to zero")


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")

#2________ Primer_____________________________________________

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be less then or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("rate cant be less then or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cant be less then or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")