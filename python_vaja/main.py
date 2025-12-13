item = input("kaj hoces kupiti?: ")
price = float(input("koliko je cena?: "))
quantity = int(input("koliko jih hoces kupti?: "))
total = price * quantity

print(f"kupil si {quantity} x {item}/s")
print(f"Kostale so te {total}€")