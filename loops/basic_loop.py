# loops_methods.py

# Create a sample list
my_list = [1, 2, 3, 4, 5]

# For loop to iterate over a list
for item in my_list:
    print("Item from list:", item)

# For loop with index using enumerate
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# Create a sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# For loop to iterate over dictionary keys
for key in my_dict:
    print("Key from dict:", key)

# For loop to iterate over dictionary values
for value in my_dict.values():
    print("Value from dict:", value)

# For loop to iterate over dictionary key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Nested for loops example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print("Element from matrix:", element)

# For loop with a range
for i in range(5):
    print("Number in range:", i)

# For loop with a specific start and end in range
for i in range(2, 10, 2):
    print("Even number in range:", i)
