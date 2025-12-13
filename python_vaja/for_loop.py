#foor loops = execute a block of code a fixed number of times.
#               you can iterate over a range, string, sequence, etc.


for x in reversed(range(1, 11)):
    print(x)

print("happy new year!")


for x in (range(1, 11, 2)):
    print(x)

credit_card = "1234-5431-2345-6444"
for x in credit_card:
    print(x)


for x in range(1, 21):
    if x ==13:
        continue
    else:
        print(x)
        