# Numbers
integer_num = 1234               # Integer
float_num = 3.14                 # Float
complex_num = 3 + 4j             # Complex number
binary_num = 0b11                # Binary number
from decimal import Decimal
decimal_num = Decimal('10.5')    # Decimal
from fractions import Fraction
fraction_num = Fraction(1, 3)    # Fraction

# String
string1 = 'spam'                 # String with single quotes
string2 = "Bob's"                # String with double quotes
byte_string = b"a\x01c"          # Byte string

# List
list_example = [1, 2, 3, [9, 10]]  # List with nested list

# Tuple
tuple_example = (1, 'spam', 4, 'U')  # Tuple with mixed data types

# Dictionary
dict1 = {'food': 'spam', 'taste': 'yum'}  # Dictionary with key-value pairs
dict2 = dict(hours=10)                    # Dictionary using the dict() function

# Boolean
bool_true = True   # Boolean True
bool_false = False # Boolean False

# None
none_example = None  # NoneType

# File
file_example = open('filename.txt', 'r')      # File opened in read mode
binary_file = open(r'C:\Users', 'wb')  # File opened in binary write mode

# Functions
def greet(name):
    return f"Hello, {name}!"   # Function definition and return statement

# Modules
import math
result = math.sqrt(16)        # Using a function from the math module

# Classes
class Dog:
    def __init__(self, name):
        self.name = name      # Constructor method

    def bark(self):
        return "Woof!"        # Method in class

my_dog = Dog("Buddy")
print(my_dog.bark())          # Creating an instance and calling a method

# Decorators
def decorator_function(func):
    def wrapper():
        print("Function is about to run")
        func()
        print("Function has finished running")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()                   # Using a decorator

# Generators
def count_up_to(max):
    count = 1
    while count <= max:
        yield count           # Yield statement
        count += 1

for number in count_up_to(5):
    print(number)             # Iterating over a generator

# Iterators
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(1, 5)
for number in counter:
    print(number)             # Custom iterator

# MetaProgramming
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super(Meta, cls).__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

my_instance = MyClass()       # Class created with a metaclass
 