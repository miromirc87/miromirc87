
#1_____Primer______________________________________


import time

time.sleep(3)

print("Times up")


#2______Primer____________________________________

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(0.5)

print("Times up")

#3________Primer______________________________________

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("Times up")

#4_________Primer__________________________________________

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up")