import math

class Solution:
    def sumOfDivisors(self, n):
        def f(n):
            size = int(math.sqrt(n))
            result = []
            
            for i in range(1, size + 1):
                if n % i == 0:
                    result.append(i)
                    if i != n // i:
                        result.append(n // i)
            # print(result)
            return sum(result)
        
        
        sum_of_allDivisors = 0
        for i in range(1, n + 1):
            sum_of_allDivisors += f(i)
            
            
        return sum_of_allDivisors
    
# Create an instance of the Solution class
solution = Solution()

# Calculate the sum of all divisors for numbers from 1 to 10
result = solution.sumOfDivisors(7)

# Print the result
print(f"The sum of all divisors for numbers from 1 to 10 is {result}")