# Creating a nested dictionary
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    }
}

# Accessing values
alice_age = nested_dict["person1"]["age"]
print("Alice's age:", alice_age)  # Output: Alice's age: 30

# Modifying values
nested_dict["person1"]["age"] = 31
print("Updated Alice's age:", nested_dict["person1"]["age"])  # Output: Updated Alice's age: 31

# Adding new entries
nested_dict["person3"] = {
    "name": "Charlie",
    "age": 28,
    "city": "Chicago"
}
print("Added Charlie:", nested_dict["person3"])  # Output: Added Charlie: {'name': 'Charlie', 'age': 28, 'city': 'Chicago'}

# Removing entries
del nested_dict["person2"]
print("After removing Bob:", nested_dict)  # Output: After removing Bob: {'person1': {'name': 'Alice', 'age': 31, 'city': 'New York'}, 'person3': {'name': 'Charlie', 'age': 28, 'city': 'Chicago'}}

# Iterating through a nested dictionary
for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
# Output:
# person1:
#   name: Alice
#   age: 31
#   city: New York
# person3:
#   name: Charlie
#   age: 28
#   city: Chicago
