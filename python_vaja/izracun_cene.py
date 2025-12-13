def stara_cena(nova_cena, popust):
    formula = 1 + (popust / 100)
    return nova_cena * formula

cena = float(input("Vnesi novo ceno izdelka: "))
popust = float(input("Vnesi popust v %: "))

print(f"Stara cena izdelka je: {stara_cena(cena, popust):.2f} EUR")


