# * Create an empty array
empty_array = []

# * Create a filled arrau
filled_array = ["A", "B", "C"]

print("\n")
print("Accessing Elements")
print("\n")
# ? Method: Add
# * Add an element to the end of the array
empty_array.append("A")
print(f"Add an element to the end of the array: {empty_array}")  # Output: ['A']

# ? Method: Insert
# * Insert an element at a specific index
empty_array.insert(0, "B")
print(f"Insert an element at a specific index: {empty_array}")  # Output: ['B', 'A']

# ? Method: Remove
# * Remove an element by value (only the first occurrence)
empty_array.remove("B")
print(f"Remove an element by value: {empty_array}")  # Output: ['A']

# ? Method: Pop
# * Remove an element by index (default is the last element)
empty_array.pop(0)
print(f"Remove an element by index: {empty_array}")  # Output: []

print("\n")
print("List Comprehension")
print("\n")
#! List Comprehension
# * Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(
    f"Create a list of numbers from 0 to 9: {numbers}"
)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# * Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(
    f"Create a list of even numbers from 0 to 9: {even_numbers}"
)  # Output: [0, 2, 4, 6, 8]

# * Create a list of squares from 0 to 9
squares = [i**2 for i in range(10)]
print(
    f"Create a list of squares from 0 to 9: {squares}"
)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# * Create a list of squares from 0 to 9, but only if the number is even
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(
    f"Create a list of squares from 0 to 9, but only if the number is even: {even_squares}"
)  # Output: [0, 4, 16, 36, 64]

# * Create a list of squares from 0 to 9, but only if the number is even, and the number is greater than 4
even_squares_greater_than_4 = [i**2 for i in range(10) if i % 2 == 0 and i > 4]
print(
    f"Create a list of squares from 0 to 9, but only if the number is even, and the number is greater than 4: {even_squares_greater_than_4}"
)  # Output: [16, 36, 64]


print("\n")
print("Slicing Arrays")
print("\n")
#! Slicing Arrays
# * Create an array of numbers from 0 to 9
numbers = [i for i in range(10)]
print(
    f"Create an array of numbers from 0 to 9: {numbers}"
)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# * Get the first element
first_element = numbers[0]
print(f"Get the first element: {first_element}")  # Output: 0

# * Get the last element
last_element = numbers[-1]
print(f"Get the last element: {last_element}")  # Output: 9

# * Get the first 3 elements
first_3_elements = numbers[:3]
print(f"Get the first 3 elements: {first_3_elements}")  # Output: [0, 1, 2]

# * Get the last 3 elements
last_3_elements = numbers[-3:]
print(f"Get the last 3 elements: {last_3_elements}")  # Output: [7, 8, 9]

# * Get the elements from index 2 to 5
elements_2_to_5 = numbers[2:6]
print(f"Get the elements from index 2 to 5: {elements_2_to_5}")  # Output: [2, 3, 4, 5]

# * Get the elements from index 2 to 5, but only every other element
elements_2_to_5_every_other = numbers[2:6:2]
print(
    f"Get the elements from index 2 to 5, but only every other element: {elements_2_to_5_every_other}"
)  # Output: [2, 4]

# * Reverse the array
reversed_array = numbers[::-1]
print(f"Reverse the array: {reversed_array}")  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# * Reverse the array, but only every other element
reversed_array_every_other = numbers[::-2]
print(
    f"Reverse the array, but only every other element: {reversed_array_every_other}"
)  # Output: [9, 7, 5, 3, 1]

# * Reverse the array, but only the first 5 elements
reversed_array_first_5 = numbers[5::-1]
print(
    f"Reverse the array, but only the first 5 elements: {reversed_array_first_5}"
)  # Output: [5, 4, 3, 2, 1, 0]

# * Reverse the array, but only the last 5 elements
reversed_array_last_5 = numbers[:-6:-1]
print(
    f"Reverse the array, but only the last 5 elements: {reversed_array_last_5}"
)  # Output: [9, 8, 7, 6, 5]

# * Reverse the array, but only the first 5 elements, and only every other element
reversed_array_first_5_every_other = numbers[5::-2]
print(
    f"Reverse the array, but only the first 5 elements, and only every other element: {reversed_array_first_5_every_other}"
)  # Output: [5, 3, 1]

# * Reverse the array, but only the last 5 elements, and only every other element
reversed_array_last_5_every_other = numbers[:-6:-2]
print(
    f"Reverse the array, but only the last 5 elements, and only every other element: {reversed_array_last_5_every_other}"
)  # Output: [9, 7, 5]
