class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxi = 0

        for num in nums_set:
            if num - 1  not in nums_set:
                current = num
                count = 1
                while current + 1 in nums_set:
                    current += 1
                    count += 1
                
                maxi = max(maxi, count)
        
        return maxi
        