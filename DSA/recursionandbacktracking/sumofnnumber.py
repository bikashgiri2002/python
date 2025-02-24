def sumOfNumbers(n):
    if n == 1:
        return 1
    return n + sumOfNumbers(n - 1)

# Test the function
print(sumOfNumbers(5)) # Output: 15