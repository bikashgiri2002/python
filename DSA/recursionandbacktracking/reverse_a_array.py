def reverseAArray(arr, si, ei):
    if si < ei:
        arr[si], arr[ei] = arr[ei], arr[si]
        reverseAArray(arr, si + 1, ei - 1)
    return arr

# Test the function
arr = [1, 2, 3, 4, 5, 6]

print("Original array:", arr)

arr = reverseAArray(arr, 0, len(arr) - 1)

print("Reversed array:", arr) # Output: [6, 5, 4, 3, 2, 1]

