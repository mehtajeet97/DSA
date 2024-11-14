from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create Hashset for first number
        visited = set(nums1)

        res =[]
        # Compare each element in second number whether in Hashset
        for i in nums2:
            if i in visited:
                res.append(i)
                # Remove Present elements from set for duplication
                visited.remove(i) 
        
        return res