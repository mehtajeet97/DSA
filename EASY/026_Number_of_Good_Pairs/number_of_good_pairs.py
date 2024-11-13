from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count ={}
        for n in nums:
            # Check number is already present in Hashmap
            # Add the frequency to result
            if n in count:
                res = res + count[n]
                count[n] = count[n]+1
            # Number not present then add it to hashmap
            else:
                count[n] = 1
        return res