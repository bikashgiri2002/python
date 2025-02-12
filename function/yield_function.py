# generator function
def fibo() :
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_sequence = fibo()

# Print the first 10 numbers in the Fibonacci sequence

for i in range(10) :
    print(next(fibonacci_sequence))