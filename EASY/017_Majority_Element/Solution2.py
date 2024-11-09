# Use a hash table
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxcount = 0, 0
        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num] > maxcount:
                res = num
            maxcount = max(count[num], maxcount)
        return res

