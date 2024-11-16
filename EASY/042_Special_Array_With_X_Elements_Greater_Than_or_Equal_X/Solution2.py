#Single Pass (Loop)
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums)+1)
        for n in nums:
            index = min(n, len(nums))
            count[index] += 1
        
        totalright = 0
        for i in reversed(range(len(nums)+1)):
            totalright += count[i]
            if i == totalright:
                return totalright
        return -1