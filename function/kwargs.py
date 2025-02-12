def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
greet(name="Alice", age=30, city="New York")

# Output:
# name: Alice
# age: 30
# city: New York
