# Sliding Window

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, end = 0, 0
        flip = 1
        zerocount = 0
        maxconsecutive = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zerocount = zerocount+1
            
            while zerocount > flip:
                if nums[start] == 0:
                    zerocount = zerocount-1
                start = start+1
            
            maxconsecutive = max(maxconsecutive, end-start+1)
            
        return maxconsecutive