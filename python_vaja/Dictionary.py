#Dictionary = a collection of {key:value} pairs
#           prdered and changable. No duplicates

capitals = {"Slovenija": "Ljubljana",
            "China": "Beijing",
            "Rusia": "Moscow"}

#print(dir(capitals))
print(help(capitals))
capitals.get("Slovenija")
capitals.get("China")
capitals.get("Rusia")

# if capitals.get ("Slovenija"):
#     print("That capital exists")
#     print(capitals.get("Slovenija"))
# else:
#     print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
print(capitals)