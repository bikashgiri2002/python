n = int(input("Enter a number: "))
n1 = n
size = len(str(n))
sum = 0

while n1 != 0:
    digit = n1 % 10
    sum += digit ** size
    n1 //= 10

if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")