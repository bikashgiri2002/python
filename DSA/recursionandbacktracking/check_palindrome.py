def checkPalindrome(str, si, ei):
    # Base case: if the subarray is of length 1 or 0, it's a palindrome
    if si >= ei:
        return True

    # If the characters at the start and end of the subarray are not equal,
    # then it's not a palindrome
    if str[si] != str[ei]:
        return False
    
    # Recursively check the subarray excluding the first and last characters
    return checkPalindrome(str, si + 1, ei - 1)

# Test the function
str = "madam"

# Convert the string to lowercase for case-insensitive comparison
str = str.lower()

# Check if the string is a palindrome

if checkPalindrome(str, 0, len(str) - 1):
    print(str, "is a palindrome.")
else:
    print(str, "is not a palindrome.")
# Output: madam is a palindrome.

# Test with a non-palindrome string

str = "hello"

if checkPalindrome(str, 0, len(str) - 1):
    print(str, "is a palindrome.")
else:
    print(str, "is not a palindrome.")
    # Output: hello is not a palindrome.