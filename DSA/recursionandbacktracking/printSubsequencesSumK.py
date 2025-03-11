class Solution:
    def printSubsequencesSumK(self, nums: list[int],index : int, target: int, sum : int, array : list[int]):
        if index == len(nums):
            if sum == target:
                print(array)
            return
        array.append(nums[index])
        sum += array[index]
        self.printSubsequencesSumK(nums, index + 1, target, sum, array)
        sum -= array.pop()
        self.printSubsequencesSumK(nums, index + 1, target, sum, array)

nums = [1, 2, 3]

target = 4

solution = Solution()

solution.printSubsequencesSumK(nums, 0, target, 0, [])
