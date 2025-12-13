pret={"1": lambda x: x * 1000 , 
      "2": lambda x: x / 1000 }

#Funkcije

def print_menu():
    print("\n##################################")
    print("- Za kilometre v metre izberite 1.")
    print("- Za metre v kilometre izberite 2.")
    print("##################################")

def izberi_operaterja():
    while True:
        pretvornik=input("\nizbira: ")
        if pretvornik in pret:
            return pretvornik
        print("napacen pretvornik")

def vnesi_razdaljo():
    while True:
        try:
            x = float(input("Vpiši razdaljo: "))
            if x < 0:
                print("Vnesi pozitivno število")
                continue
            elif x == 0:
                print("0? A ti to res?")
                continue
            return x
        except ValueError:
            print("Napačen vnos, vnesi število")

def ponovni_zagon():
    znova=input("A zelis vnesti novo dolzino? (y/n)").lower()
    return znova =="y"

#Main

while True:   
    #izpise menu za izbiro operaterja
    print_menu()
    
    #poslje podatek želene izbire
    pretvornik=izberi_operaterja()
    
    #poda razdaljo za pretvorbo
    x=vnesi_razdaljo()
    
    #ustvari vrednost pripravljeno za izpis
    rezultat=pret[pretvornik](x)
        

        
    if pretvornik == "1":
        print(f" {rezultat:.2f} m")
    else: 
        print(f" {rezultat:.3f} km")    
    if not ponovni_zagon():
        break


