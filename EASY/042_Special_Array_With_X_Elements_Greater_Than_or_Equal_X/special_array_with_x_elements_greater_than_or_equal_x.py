from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #Sort the Array
        nums.sort()
        i = 0
        prev = -1
        totalright = len(nums)
        # Check Number between previous and count ahead
        while i < len(nums):
            if nums[i] == totalright or (prev < totalright < nums[i]):
                return totalright

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            prev = nums[i]
            i += 1
            totalright = len(nums) - i

        return -1
