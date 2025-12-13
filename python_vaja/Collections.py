#collection = single variable used to store multiple values

#List = [] ordered and changeable. Duplicate OK
#Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER



#1______________________List__________________________________

#fruits = ['apple', 'banana', 'orange', 'coconut']

#print(fruits[1])
#print(fruits[0:3])
#print(fruits[::2])      #vsak drugi
#print(fruits[::-1])     #vzvratno

#for x in fruits:
#    print(fruits)


#dir(fruits)
#print(dir(fruits))


#help(fruits)

#print(len(fruits)) #koliko sadja v kolekciji

#print("apple" in fruits)    #True / False

#fruits.append("kivi")
#print(fruits)

#fruits.insert(5, "grape")
#print(fruits)
#fruits.remove("grape")

#fruits.sort()

#fruits.reverse()
#print(fruits)

#print(fruits.index("kivi"))

#2________________Set_________________________________________

#fruits = {"apple", "orange", "banana", "coconut"}

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#fruits.add("pineapple")        #doda "xxxx"
#fruits.remove("apple")         #odstrani "XXXX"
#fruits.pop()                   #odstrani random
#fruits.clear()                 #ostranit

#print(fruits)

#3__________________Tuple_______________________________________

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
#print(fruits.count("coconut"))

#print(fruits)