#format_specifiers = {value_flags} format a value based on what flags are inserted

# format specifiers = {:flags} format a value based on what flags are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3.141
price2 = -987.65
price3 = 12.34
price4 = 3175353474567.123
price5 = 4234.3

#print(f"Price 1 is ${price1:.2f}")
#print(f"Price 2 is ${price2:.2f}")
#print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:+7}")
print(f"price 4 is ${price4:40,}")
print(f"price 5 is ${price5:.2f}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 2 is ${price2:>10}")