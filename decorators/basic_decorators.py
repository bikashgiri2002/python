def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

# Using the decorated function
greet("Bhagya")

# Output:
# Before the function call
# Hello, Bhagya!
# After the function call
