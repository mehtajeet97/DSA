# Two Sets, Single Pass(Loop) Solution
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Create hashset for unique values
        set1, set2 = set(nums1), set(nums2)
        # Remove common values found in both the sets
        for n in nums1:
            if n in set2:
                set1.remove(n)
                set2.remove(n)

        return [list(set1), list(set2)]