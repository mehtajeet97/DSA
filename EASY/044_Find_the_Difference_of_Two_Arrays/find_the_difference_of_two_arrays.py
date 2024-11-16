# Creation of 4 sets

from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Create hashset for unique values
        set1, set2 = set(nums1), set(nums2)
        # Store output in set as well to avoid duplication
        res1, res2 = set(), set()

        for n in nums1:
            if n not in set2:
                res1.add(n)
        
        for n in nums2:
            if n not in set1:
                res2.add(n)
                
        return [list(res1), list(res2)]