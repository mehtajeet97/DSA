# Sorting method - First sort the array and then check neighbors
# Time : O(n * logn)
# Space : O(1)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False