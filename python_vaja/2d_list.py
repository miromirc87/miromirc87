# 2d Lists
#from Collections import fruits

# fruits = ['apple', 'banana', 'orange']
# vegetables = ["carrot", "potatoes", "celery"]
# meats = ["chicken", "fish", "turkey"]
#
# groceries = [fruits, vegetables, meats]

#fruits[0] = "pineapple"

# print(groceries[0][0])
# print(groceries[1][1])
# print(groceries[2][2])
# print(groceries[0][2])

# for g in groceries:
#     print(g[0], end="\t")


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", "0", "#"))

for row in num_pad:
    for num in row:
       print(num, end=' ')
    print()
