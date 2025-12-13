# Menu Ordering System

# Menu dictionary with item names and prices
menu = {
        "pica": 3.00,
        "nachosi": 4.50,
        "kokice": 6.00,
        "pomfri": 2.50,
        "čips": 1.00,
        "limonada": 2.30,
        "cocta": 3.25
        }

# Initialize cart and total
cart = []
total = 0

# Print the menu
print("--------MENU-------")
for key, value in menu.items():
        print(f" {key:10}: €{value:.2f}")
print("-------------------")

# Main order-taking loop
while True:
        food = input("Select an item (q to quit): ").lower()  # User input (case-insensitive)

        # Quit the loop if the user types 'q'
        if food == "q":
                break
        # Check if the input is a valid menu item
        elif menu.get(food) is not None:
                cart.append(food)  # Add valid item to the cart
        else:
                print("Invalid item, please try again!")  # Handle invalid input

# Display the order summary
print("\n---------Order----------")
for food in cart:
        total += menu.get(food)  # Add item price to the total
        print(food, end=" * ")  # Print item names in a single line

# Print the total cost
print("\n------------------------")
print(f"Total is: €{total:.2f}")
