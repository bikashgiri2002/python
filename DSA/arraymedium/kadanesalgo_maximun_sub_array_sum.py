def maxSubarraySum(arr, n) :

	# Your code here
    j = 0
    total = 0
    maxi = 0
    for i in range(n):
        total += arr[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
            j = i
    return maxi

def maxSubarraySumAndPrint(arr, n) :

	# Your code here
    left = 0
    right = 0
    total = 0
    maxi = 0
    for i in range(n):
        total += arr[i]
        if total > maxi:
            maxi = total
            left = i + 1
        if total < 0:
            total = 0
            right = i + 1
        i += 1
    print("Max subarray sum is: ", maxi)
    print("Subarray is: ", arr[right:left])

# Test the function
arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
# arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)
print(maxSubarraySum(arr, n))

# Test the function with printing the subarray
maxSubarraySumAndPrint(arr, n)