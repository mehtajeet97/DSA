from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #Largest & Second Largest Variables
        max1, max2 = 0, 0
        #Smallest & Second Smallest Variables
        min1 = min2 = float("inf")
        
        # Check number greater or less than Variables in One Iteration
        for n in nums:
            if n > max2:
                if n > max1:
                    max2 = max1
                    max1 = n
                else:
                    max2 = n
            
            if n < min2:
                if n < min1:
                    min2 = min1
                    min1 = n
                else:
                    min2 = n
        
        return (max2 * max1) - (min1 * min2)