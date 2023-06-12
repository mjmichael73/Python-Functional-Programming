from functools import reduce


# Defining a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Calculate the square of each number by using map and a lambda function
squared_numbers = map(lambda x: x**2, numbers_list)

# Find even numbers by applying a lambda function
even_numbers = filter(lambda x: x % 2 == 0, numbers_list)

# Find the product of all numbers in the list using reduce and a lambda function
numbers_producted = reduce(lambda x, y: x * y, numbers_list)


# Result

print(f"Numbers list: {numbers_list}")
print(f"Squared numbers list: {list(squared_numbers)}")
print(f"Even numbers list: {list(even_numbers)}")
print(f"Product of all numbers: {numbers_producted}")
