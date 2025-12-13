nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

def get_evens(input_list):
    return list(filter(lambda x: x % 2 == 0, input_list))
print(get_evens([11,12,13,14,15,16,17,18,19,20]))

def get_evens(input_list):
    evens = []
    for num in input_list:
        if num % 2 == 0:
            evens.append(num)
    return evens