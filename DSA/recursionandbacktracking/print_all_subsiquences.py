def printAllsubsiqueness(nums : list[int], index : int, arr : list[int]):
    if index == len(nums):
        print(arr)
        return
    arr.append(nums[index])
    printAllsubsiqueness(nums, index + 1, arr)
    arr.pop()
    printAllsubsiqueness(nums, index + 1, arr)

nums = [3, 1, 2]
arr = []

printAllsubsiqueness(nums, 0, arr)
