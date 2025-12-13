#database

class InventoryDatabase:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                raise ValueError("Not enough items in inventory to remove.")
        else:
            raise KeyError("Item not found in inventory.")

    def get_inventory(self):
        return self.items
    
#interface

def print_menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")

def get_user_choice():
    while True:
        choice = input("Choose an option (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice, please try again.")

def get_item_details():
    item_name = input("Enter item name: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                return item_name, quantity
            else:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input, please enter a number.")
#main

def main():
    db = InventoryDatabase()
    while True:
        print_menu()
        choice = get_user_choice()
        if choice == '1':
            item_name, quantity = get_item_details()
            db.add_item(item_name, quantity)
            print(f"Added {quantity} of {item_name}.")
        elif choice == '2':
            item_name, quantity = get_item_details()
            try:
                db.remove_item(item_name, quantity)
                print(f"Removed {quantity} of {item_name}.")
            except (ValueError, KeyError) as e:
                print(e)
        elif choice == '3':
            inventory = db.get_inventory()
            if inventory:
                print("Current Inventory:")
                for item, qty in inventory.items():
                    print(f"{item}: {qty}")
            else:
                print("Inventory is empty.")
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break

if __name__ == "__main__":
    main()
