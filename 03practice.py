# https://www.makeuseof.com/tag/python-lambda-functions/

def add_number(number):
    return number + 5

print(add_number(12))

add_number2 = lambda number: number + x

print(add_number(number=-11))

add_2number = lambda x, y: x + y + 5

print(add_2number(x=-5, y=1))

#
#
#

def square_root(x):
    return x ** (1/2)

numbers = [1,2,3,4,5]

print(numbers)

# map: expects two arguments: a function and a list. takes that function and applies
#      it to every element in the list, returning the list of modified elements as a map
#      object
# list: convert the resulting map object back into a list

new_numbers = list(map(square_root,numbers))

print(new_numbers)

#
#
#

numbers2 = [1,2,3,4,5]

print(numbers2)

new_numbers2 = list(map(lambda x: x ** (1/2), numbers2))

print(new_numbers2)
