#Shopping cart program


foods =[]
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit) : ")
    if food.lower() =="q":                              #spremeni Q v q .lower()
        break
    else:
        price= float(input(f"Enter the price of a {food}:$"))
        foods.append(food)
        prices.append(float(price))

print ("------- YOUR CART ------")

for food in foods:
    print(food, end="\t")

for price in prices:
    total = total + price
  #  total += price

print()
print(f"your total is: ${total}")


# ___________________________________________________________________




# foods = []  # List to store food items
# prices = []  # List to store prices
#
# while True:
#     food = input("Enter food to buy (q to quit): ")
#     if food.lower() == "q":  # Checks for 'q' in any case
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(float(price))
#
# # Print YOUR CART with items separated by spaces
# print("------- YOUR CART ------")
# print(" ".join(foods))
#
# # Print YOUR CART with items separated by tabs
# print("------- YOUR CART ------")
# print("\t".join(foods))

# _________________________________________________________________

# words = ["I", "like", "to", "code"]
# sentence = " ".join(words)
# print(sentence)  # Output: "I like to code"