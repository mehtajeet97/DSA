from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        # Map the occurence of each number in Map
        count = Counter(nums)
        
        # Loop through all numbers from 1 to the length of nums
        # Check which number has zero occurence and one which has twice occurence
        for i in range(1, len(nums)+1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i
        
        return res
