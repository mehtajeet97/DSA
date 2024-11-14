# Math Solution

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # Duplicate - Missing = X
        x = 0 
        # Duplicate^2 - Missing^2 = Y
        y = 0
        
        # Find the value for X and Y through Looping
        for i in range(1, N+1):
            x += nums[i-1] - i
            y += nums[i-1]**2 - i**2

        # Find Missing and Duplicate once X & Y are found
        missing = (y - x**2)// (2*x)
        duplicate = missing + x

        return [duplicate, missing]