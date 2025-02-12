def outer_function(text):
    def inner_function():
        print(text)
    return inner_function

# Create a closure
closure = outer_function("Hello, world!")
closure()  # Output: Hello, world!
