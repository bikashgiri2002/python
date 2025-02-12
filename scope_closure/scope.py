x = "global"

def outer_function():
    x = "enclosing"

    def inner_function():
        x = "local"
        print("Inner:", x)
    
    inner_function()
    print("Outer:", x)

outer_function()
print("Global:", x)

# Output:
# Inner: local
# Outer: enclosing
# Global: global

# Global variable
count = 0

def increment():
    global count  # Declare count as global
    count += 1  # Modify the global variable

def decrement():
    global count  # Declare count as global
    count -= 1  # Modify the global variable

# Using the functions
print("Initial count:", count)  # Output: Initial count: 0
increment()
print("After increment:", count)  # Output: After increment: 1
decrement()
print("After decrement:", count)  # Output: After decrement: 0
