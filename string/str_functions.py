# Initializing a string
my_string = "Hello, World!"

# 1. len() - Get the length of the string
length = len(my_string)
print(f"Length of the string: {length}")

# 2. lower() - Convert string to lowercase
lowercase_string = my_string.lower()
print(f"Lowercase: {lowercase_string}")

# 3. upper() - Convert string to uppercasen
uppercase_string = my_string.upper()
print(f"Uppercase: {uppercase_string}")

# 4. replace() - Replace a substring with another substring
replaced_string = my_string.replace("World", "Python")
print(f"Replaced string: {replaced_string}")

# 5. split() - Split the string into a list of substrings
split_string = my_string.split(", ")
print(f"Split string: {split_string}")

# 6. join() - Join a list of strings into a single string
joined_string = " ".join(split_string)
print(f"Joined string: {joined_string}")

# 7. strip() - Remove leading and trailing whitespace
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(f"Stripped string: '{stripped_string}'")

# 8. find() - Find the position of a substring in a string
position = my_string.find("World")
print(f"Position of 'World': {position}")

# 9. count() - Count occurrences of a substring in a string
count = my_string.count("l")
print(f"Occurrences of 'l': {count}")

# 10. format() - Format string using placeholders
formatted_string = "My name is {} and I am {} years old.".format("John", 30)
print(f"Formatted string: {formatted_string}")

# escape sequence
new_line = "Bhagya is a god girl\nshe is from sarathigada"
print(new_line)
