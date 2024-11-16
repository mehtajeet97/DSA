from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countneg = 0
        for n in nums :
        # Zero in the array should return zero
            if n == 0:
                return 0
            # Count Negative Numbers
            if n < 0:
                countneg += 1
        # For Odd negative numbers return -1
        if countneg%2 :
            return -1
        # Else return 1    
        else:
            return 1