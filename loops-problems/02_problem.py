n = 10

sum = 0

for i in range(n + 1):
    sum += i if(i % 2 == 0) else 0

print(sum)