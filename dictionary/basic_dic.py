# dict_example.py

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
name = my_dict["name"]
print("Name:", name)  # Output: Name: Alice

# Adding or updating entries
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing value
print("Updated dictionary:", my_dict)  
# Output: Updated dictionary: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removing entries
del my_dict["city"]  # Removing a key-value pair using del
print("Dictionary after removing 'city':", my_dict)  
# Output: Dictionary after removing 'city': {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

email = my_dict.pop("email")  # Removing and returning the value using pop
print("Removed email:", email)  # Output: Removed email: alice@example.com
print("Dictionary after removing 'email':", my_dict)  
# Output: Dictionary after removing 'email': {'name': 'Alice', 'age': 31}

# Iterating through a dictionary
print("Keys and values in the dictionary:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
# Output:
# Keys and values in the dictionary:
# name: Alice
# age: 31
print("Keys and values in the dictionary:")
# using key and value
for key, value in my_dict.items():
    print(key, value)
# Keys and values in the dictionary:
# name Alice
# age 31

# Using dictionary methods
keys = my_dict.keys()
print("Keys:", list(keys))  # Output: Keys: ['name', 'age']

values = my_dict.values()
print("Values:", list(values))  # Output: Values: ['Alice', 31]

items = my_dict.items()
print("Items:", list(items))  # Output: Items: [('name', 'Alice'), ('age', 31)]

# Using get method
age = my_dict.get("age", 0)
print("Age:", age)  # Output: Age: 31

# Filtering a dictionary (example: keeping entries with values greater than a specific threshold)
def filter_dict(d, threshold):
    return {k: v for k, v in d.items() if isinstance(v, int) and v > threshold}

filtered_dict = filter_dict(my_dict, 25)
print("Filtered dictionary (values greater than 25):", filtered_dict)  
# Output: Filtered dictionary (values greater than 25): {'age': 31}

# Merging two dictionaries
other_dict = {"occupation": "Engineer", "hobby": "Painting"}
merged_dict = {**my_dict, **other_dict}
print("Merged dictionary:", merged_dict)  
# Output: Merged dictionary: {'name': 'Alice', 'age': 31, 'occupation': 'Engineer', 'hobby': 'Painting'}
