# print n time hello world
def printHelloWorld(n):
    if n == 0:
        return 
    
    printHelloWorld(n - 1)
    print("Hello World", n)

# Test the function

printHelloWorld(5) # prints "Hello World" 5 times

def printReverse(n):
    if n == 1:
        print(n)
        return
    print(n)
    printReverse(n - 1)

# Test the function

printReverse(5) # prints 5, 4, 3, 2, 1