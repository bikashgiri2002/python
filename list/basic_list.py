# list_methods.py

# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("Append:", my_list)

# Extend the list with another list
my_list.extend([7, 8, 9])
print("Extend:", my_list)

# Insert an element at a specific position
my_list.insert(0, 0)
print("Insert:", my_list)

# Remove the first occurrence of an element
my_list.remove(5)
print("Remove:", my_list)

# Pop an element from the list (default is the last element)
popped_element = my_list.pop()
print("Pop:", my_list, "Popped element:", popped_element)

# Pop an element at a specific position
popped_element = my_list.pop(0)
print("Pop at index 0:", my_list, "Popped element:", popped_element)

# Index of the first occurrence of an element
index = my_list.index(3)
print("Index of 3:", index)

# Count the number of occurrences of an element
count = my_list.count(2)
print("Count of 2:", count)

# Sort the list in ascending order
my_list.sort()
print("Sort:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("Sort descending:", my_list)

# Reverse the list
my_list.reverse()
print("Reverse:", my_list)

# Clear all elements from the list
my_list.clear()
print("Clear:", my_list)

# Create a copy of the list
copy_list = my_list.copy()
print("Copy:", copy_list)
