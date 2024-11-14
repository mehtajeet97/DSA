# Single Pass Solution

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        
        # Flag the seen numbers as negative
        # the remaining positive number is the Duplicate
        for n in nums:
            n = abs(n)
            nums[n -1] = -nums[n-1]
            if nums[n-1] > 0:
                res[0] = n
        
        # Lopp through again to check for the Missing
        for i, n in enumerate(nums):
            if n>0 and i+1!= res[0]:
                res[1] = i+1

        return res
