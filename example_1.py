# Pure function
# Input: List of numbers
# Output: Sum of numbers
def sum_numbers(numbers_list):
    return sum(numbers_list)

# Higher order function
# Input: function, list of numbers
# Output: Applies function to list of numbers
def apply_function_to_numbers(function, numbers_list):
    return function(numbers_list)


# Test
numbers_list = [1, 2, 3, 4, 5]
sum_of_numbers = sum_numbers(numbers_list)
sum_of_numbers_functional = apply_function_to_numbers(sum_numbers, numbers_list)

print(sum_of_numbers == sum_of_numbers_functional)